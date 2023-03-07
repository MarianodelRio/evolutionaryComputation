'''
Script to implement the evolutionary operators used in the algorithm

@author: Mariano del Río
@date: 04-03-2023
'''

import numpy as np
import random as rd


def crossover(population, population_size, crossover_rate):
    new_population = []
    for i in range(0, population_size, 2):
        if rd.random() < crossover_rate:
            crossover_point = rd.randint(1, len(population[i])-1)
            child1 = np.concatenate((population[i][:crossover_point], population[i+1][crossover_point:]))
            child2 = np.concatenate((population[i+1][:crossover_point], population[i][crossover_point:]))
            new_population.append(child1)
            new_population.append(child2)
            pass
        else:
            new_population.append(population[i])
            new_population.append(population[i+1])
    return np.array(new_population)

def mutation(population, population_size, mutation_rate, search_space):
    for i in range(population_size):
        for j in range(len(population[i])):
            if rd.random() < mutation_rate:
                population[i][j] = rd.uniform(search_space[j][0], search_space[j][1])
    return population


