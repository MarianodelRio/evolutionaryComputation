'''
Implementation of the evolutionary algorithm based on aggregation fitness to solve multiobjective optimization problems.

@author: Mariano del Río 
@date: 04-03-2023
'''

import numpy as np
import random as rd 
import pandas as pd
from matplotlib import pyplot as plt

from .evolutionary_operators import gaussian_mutation

class EA:

    def __init__(self, problem, population_size,
                 generations, mutation_rate,
                 neighborhood_size, SIG):

        # Parameters 
        self.problem = problem # Fitness function, search space and dimension
        self.N = population_size
        self.m = self.problem.num_functions # Number of objectives
        self.fitness = self.problem.fitness
        self.dimension = self.problem.dimension 
        self.fitness_values = np.zeros((self.N, self.m))
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.neighborhood_size = neighborhood_size
        self.SIG = SIG
        #self.historic = np.zeros((self.generations, self.N))

    def create_weight_vectors(self):
        weight_vectors = np.zeros((self.N, self.m))
        for i in range(self.N):
            for j in range(self.m):
                weight_vectors[i][j] = i/(self.N - 1)
        return weight_vectors
    
    def create_population(self):
        population = np.zeros((self.N, self.dimension))
        for i in range(self.N):
            for j in range(self.problem.dimension):
                population[i][j] = rd.uniform(self.problem.search_space[j][0], self.problem.search_space[j][1])
        return population
    
    def create_neighborhood(self):
        neighborhood = np.zeros((self.N, self.neighborhood_size), dtype=int)
        for i in range(self.N):
            distances = np.zeros(self.N)
            for j in range(self.N):
                distances[j] = np.linalg.norm(self.population[i] - self.population[j])
            neighborhood[i] = np.argsort(distances)[:self.neighborhood_size]
            # Indexes of the nearest weight vectors
        
        return neighborhood

    def evaluate_individual(self, i):
        self.fitness_values[i] = self.fitness(self.population[i]) 

    def evaluate_population(self):
        for i in range(self.N):
            self.evaluate_individual(i)

    def create_reference_point(self):
        reference_point = np.zeros(self.m)
        for i in range(self.m):
            reference_point[i] = np.max(self.fitness_values[:, i])
            # Max value of objective function i
        return reference_point
        
    def initialize(self):
        self.weight_vectors = self.create_weight_vectors()
        self.population = self.create_population()  
        self.neighborhood = self.create_neighborhood()
        self.evaluate_population()
        self.reference_point = self.create_reference_point()

    def update_reference_point(self, i):
        fy = self.fitness_values[i]
        for i in range(len(self.reference_point)):
            if fy[i] < self.reference_point[i]:
                self.reference_point[i] = fy[i]

    def update_neighborhood(self, i):
        for j in range(self.neighborhood_size):
            gi = self.problem.g(self.population[i], self.weight_vectors[i], self.reference_point)
            gj = self.problem.g(self.population[j], self.weight_vectors[i], self.reference_point)
            if gi < gj:
                self.population[j] = self.population[i]
                self.neighborhood[i][j] = i

    def reproduce_population(self, individual):
        self.new_individual = gaussian_mutation(individual, self.problem.search_space, self.mutation_rate, self.SIG)
    
    def iteration(self, i):
        nearest_ind = self.population[self.neighborhood[i][0]]
        self.reproduce_population(nearest_ind)
        self.evaluate_individual(i)
        self.update_reference_point(i)
        self.update_neighborhood(i)
    
    def run_algorithm(self):
        self.initialize()
        #self.historic[0] = self.population
        for j in range(1, self.generations+1):
            if j % 10 == 0:
                print("Generation: ", j, "Best fitness: ", self.problem.fitness(self.get_best_individual()))
            for i in range(self.N):
                self.iteration(i)

            #self.historic[i] = self.population
        

    def get_best_individual(self):
        best_individual = self.population[np.argmin(self.fitness, axis=0)]
        return best_individual
       
    def export_historic(self, name):
        # Export historic of the population to csv file 
        #df = pd.DataFrame(self.historic)
        #df.to_csv(name, index=False)
        pass

    def plot_historic(self):
        # Plot population 
        f1 = self.fitness_values[:, 0]
        f2 = self.fitness_values[:, 1]

        plt.scatter(f1, f2, c='b')
        plt.show()
        
    
    
    

