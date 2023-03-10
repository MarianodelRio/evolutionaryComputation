'''
Script to implement the evolutionary operators used in the algorithm

@author: Mariano del Río
@date: 04-03-2023
'''

import numpy as np
import random as rd


def gaussian_mutation(individual, search_space, mutation_rate, SIG):
     
    for i in range(len(individual)):
        if rd.random() < mutation_rate:
            sigma = (search_space[i][1] - search_space[i][0]) / SIG
            individual[i] = individual[i] + rd.gauss(0, sigma)
            if individual[i] < search_space[i][0]:
                individual[i] = search_space[i][0]
            elif individual[i] > search_space[i][1]:
                individual[i] = search_space[i][1]
    return individual

def differential_evolution_crossover(parents, search_space, F, mutation_rate):
    delta = rd.randint(0, len(parents[0]) - 1)
    child = np.zeros(len(parents[0]))
    for i in range(len(parents[0])):
        if rd.random() < mutation_rate or i == delta:
            child[i] = parents[0][i] + F*(parents[1][i] - parents[2][i])
            
            if child[i] < search_space[i][0]:
                child[i] = search_space[i][0]
            elif child[i] > search_space[i][1]:
                child[i] = search_space[i][1]
        else:
            child[i] = parents[0][i]
    return child
