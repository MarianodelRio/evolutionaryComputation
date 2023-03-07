'''
Implementation of the evolutionary algorithm based on aggregation fitness to solve multiobjective optimization problems.

@author: Mariano del Río 
@date: 04-03-2023
'''

import numpy as np
import random as rd 
import pandas as pd
from .evolutionary_operators import crossover

class EA:

    def __init__(self, problem, population_size, 
                 generations, dimension, crossover_rate, 
                 mutation_rate,
                 neighborhood_size):

        # Parameters 
        self.problem = problem
        self.fitness = problem.fitness
        self.restrictions = problem.restrictions
        self.N = population_size
        self.fitness_values = np.array([np.array([0.0 for _ in range(problem.num_functions)]) for i in range(self.N)])
        self.reference_point = np.array([0.0 for _ in range(dimension)])
        self.generations = generations
        self.dimension = dimension
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.neighborhood_size = neighborhood_size
        self.search_space = problem.search_space
        #self.historic = np.zeros((self.generations, self.N))

    def initialize(self):
        self.population = self.create_population()  
        self.neighborhood = self.create_neighborhood()
        self.evaluate_population()
        self.reference_point = self.create_reference_point()
        

    def create_population(self):
        population = np.zeros((self.N, self.dimension))
        rate = [(self.search_space[i][1] - self.search_space[i][0])/self.N for i in range(self.dimension)]
        for i in range(self.N):
            for j in range(self.dimension):
                population[i][j] = self.search_space[j][0] + rate[j]*i

        return population
    
    def create_neighborhood(self):
        neighborhood = np.zeros((self.N, self.neighborhood_size, self.dimension))
        for i in range(self.N):
            distances = np.zeros(self.N)
            for j in range(self.N):
                distances[j] = np.linalg.norm(self.population[i] - self.population[j])
            neighborhood[i] = self.population[np.argsort(distances)[:self.neighborhood_size]]

        
        return neighborhood
        
    def evaluate_population(self):
        # Evaluate the fitness of the population

        for i in range(self.N):
            self.fitness_values[i] = self.fitness(self.population[i])

    def restriction_penalty(self, population):
        penalization = 1000
        loss = np.zeros((self.N, 2))
        for i in range(self.N):
            if self.restrictions(population[i]) == False:
                loss[i] = np.array([penalization, penalization])
        return loss

    def create_reference_point(self):
        reference_point = np.zeros(self.dimension)
        for i in range(self.dimension):
            reference_point[i] = np.max(self.fitness_values[:, i])
        return reference_point

    def update_reference_point(self):
        fy = self.fitness(self.get_best_individual())
        for i in range(len(self.reference_point)):
            if fy[i] < self.reference_point[i]:
                self.reference_point[i] = fy[i]

    def get_best_individual(self):
        best_individual = self.population[np.argmin(self.fitness, axis=0)]
        return best_individual
    
    def update_neighborhood(self):
        y = self.get_best_individual()
        for i in range(self.N):
            neighborhood = self.neighborhood[i]
            for j in range(len(neighborhood)):
                if self.problem.g(y, self.reference_point) < self.problem.g(neighborhood[j], self.reference_point):
                    self.neighborhood[i][j] = y

    def reproduce_population(self):
        self.population = crossover(self.population, self.N, self.crossover_rate)


    def get_fitness(self):
        return self.fitness
    
    def get_population(self):
        return self.population
    
    def get_reference_point(self):
        return self.reference_point
    
    
    def iteration(self):
        self.reproduce_population()
        self.evaluate_population()
        self.update_reference_point()
        self.update_neighborhood()
    
    def run_algorithm(self):
        self.initialize()
        #self.historic[0] = self.population
        for i in range(1, self.generations):
            print("Generation: ", i, "Best fitness: ", self.fitness(self.get_best_individual()), "Individual: ", self.get_best_individual())
            self.iteration()
            #self.historic[i] = self.population
        #return self.population, self.fitness
    
    def export_historic(self, name):
        # Export historic of the population to csv file 
        #df = pd.DataFrame(self.historic)
        #df.to_csv(name, index=False)
        pass

    def plot_historic(self):
        # Plot historic of the population
        pass
    
    
    

