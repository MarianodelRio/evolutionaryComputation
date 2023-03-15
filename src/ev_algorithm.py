'''
Implementation of the evolutionary algorithm based on aggregation fitness to solve multiobjective optimization problems.

@author: Mariano del Río 
@date: 04-03-2023
'''

import numpy as np
import random as rd 
import pandas as pd
from matplotlib import pyplot as plt
import time
from .evolutionary_operators import gaussian_mutation, differential_evolution_crossover

class EA:

    def __init__(self, problem, population_size,
                 generations, mutation_rate,
                 neighborhood_size, SIG, F):

        # Parameters 
        self.problem = problem # Fitness function, search space and dimension
        self.N = population_size
        self.m = self.problem.num_functions # Number of objectives
        self.fitness = self.problem.fitness
        self.dimension = self.problem.dimension 
        self.fitness_values = np.zeros((self.N, self.m + 1))
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.neighborhood_size = neighborhood_size
        self.SIG = SIG
        self.F = F
        self.historic = np.zeros((self.generations * self.N, self.m + 1))

    def create_weight_vectors(self):
        weight_vectors = np.zeros((self.N, self.m))
        for i in range(self.N):
            for j in range(self.m):
                weight_vectors[i][j] = (i+1)/(self.N+1)
        
        for i in range(self.N):
            weight_vectors[i][0] = weight_vectors[self.N - i - 1][1]

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
            reference_point[i] = np.min(self.fitness_values[:, i])
            # Max value of objective function i
        return reference_point
        
    def initialize(self):
        self.weight_vectors = self.create_weight_vectors()
        self.population = self.create_population()  
        self.neighborhood = self.create_neighborhood()
        self.evaluate_population()
        self.reference_point = self.create_reference_point()

    def update_reference_point(self, new_fitness):
        fy = new_fitness
        for i in range(len(self.reference_point)):
            if fy[i] < self.reference_point[i]:
                self.reference_point[i] = fy[i]

    def update_neighborhood(self, i, new_individual, new_fitness):
        
        for j in range(self.neighborhood_size):
            index_neigh = self.neighborhood[i][j]
            gn = self.problem.g(new_fitness, self.weight_vectors[index_neigh], self.reference_point)           
            gj = self.problem.g(self.fitness_values[index_neigh], self.weight_vectors[index_neigh], self.reference_point)

            if gn < gj:
                self.population[index_neigh] = new_individual
                self.fitness_values[index_neigh] = new_fitness
            else: 
                self.fitness_values[index_neigh] = self.fitness(self.population[index_neigh])


    def reproduce_population(self, individual1, individual2, individual3):
        new_individual = differential_evolution_crossover([individual1, individual2, individual3], 
                                                          self.problem.search_space, self.mutation_rate, self.F)
        new_individual = gaussian_mutation(new_individual, self.problem.search_space, self.mutation_rate, self.SIG)
        
        new_fitness = self.problem.fitness(new_individual)
        return new_individual, new_fitness
    
    def iteration(self, i):
        i1, i2, i3 = np.random.choice(self.neighborhood[i], 3, replace=False)
        neigh1 = self.population[i1]
        neigh2 = self.population[i2]
        neigh3 = self.population[i3]
        new_individual, new_fitness = self.reproduce_population(neigh1, neigh2, neigh3)
        self.update_reference_point(new_fitness)
        self.update_neighborhood(i, new_individual, new_fitness)
    
    def run_algorithm(self):
        self.initialize()
        for k in range(self.N):
            self.historic[k] = self.fitness_values[k]
        
        for j in range(1, self.generations):
            if j % 10 == 0:
                print("Generation: ", j)
                
            # Generate plot loop 
            plt.cla()
            plt.xlim(-0.10, 1.1)
            plt.ylim(-2,3)
            f1 = self.fitness_values[:, 0]
            f2 = self.fitness_values[:, 1]
            self.problem.plot_ideal_front()
            plt.scatter(f1, f2, c='black', s=2)
            plt.xlabel('f1')
            plt.ylabel('f2')
            plt.pause(0.0001)


            for i in range(self.N):
                self.iteration(i)

            self.historic = np.vstack([self.historic, self.fitness_values])
        
       
    def export_historic(self, name):
        with open(name, 'w') as f:
            np.savetxt(name, self.historic, fmt='%.6e', delimiter=' ', footer='')

    def plot_historic(self):
        # Plot population 
        f1 = self.fitness_values[:, 0]
        f2 = self.fitness_values[:, 1]

        plt.scatter(f1, f2, c='b')
        plt.show()
        # Keep one second and close the plot
        time.sleep(1)
        plt.close()
        
    
    
    

