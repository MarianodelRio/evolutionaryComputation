'''
Script to implement functions to optimize via evolutionary algorithms

@author: Mariano del Río
@date: 04-03-2023
'''

import numpy as np
from matplotlib import pyplot as plt

class ZDT3:

    def __init__(self, dimension):
        self.name = 'ZDT3'
        self.dimension = dimension
        self.search_space = self.create_search_space()
        self.num_functions = 2

    def f1(self, x):
        return x[0]

    def f2(self, x):
        g = 1 + (9 / (self.dimension - 1)) * np.sum(x[1:]) 
        h = 1 - np.sqrt(self.f1(x) / g) - (self.f1(x) / g) * np.sin(10 * np.pi * self.f1(x))
        return g * h
    
    def c1(self, x):
        return 0.0
    
    def c2(self, x):
        return 0.0
    
    def fitness(self, individual):
        return np.array([self.f1(individual), self.f2(individual), 0.0])
    
    def create_search_space(self):
        search_space = np.zeros((self.dimension, 2))
        for i in range(self.dimension):
            search_space[i][0] = 0
            search_space[i][1] = 1
        return search_space
    
    def g(self, weight_vector, ref_point, fitness):
        return np.max([weight_vector[j] * np.abs(fitness[j] - ref_point[j]) for j in range(self.num_functions)])
    
    def plot_ideal_front(self):

        f1 = np.concatenate((np.linspace(0, 0.0830015349, 20), np.linspace(0.1822287280, 0.2577623634, 20) ,np.linspace(0.4093136748, 0.4538821041, 20), np.linspace(0.6183967944, 0.6525117038, 20), np.linspace(0.8233317983, 0.8518328654, 20)), axis=0)
        
        f2 = 1 - np.sqrt(f1) - f1 * np.sin(10 * np.pi * f1)

        plt.scatter(f1, f2, color='blue', s=2, label='Ideal Front')
        
    
    def plot_function(self):
        population = np.zeros((100, self.dimension))
        f1 = np.zeros(100)
        f2 = np.zeros(100)

        for i in range(100):
            for j in range(self.dimension):
                population[i][j] = np.random.uniform(self.search_space[j][0], self.search_space[j][1])
                
            f1[i] = self.f1(population[i])
            f2[i] = self.f2(population[i])
        
        plt.scatter(f1, f2, color='blue', s=0.7)

class CF6:

    def __init__(self, dimension, cons_method = 'penalization'):
        self.name = 'CF6'
        self.dimension = dimension
        self.search_space = self.create_search_space()
        self.num_functions = 2
        self.cons_method = cons_method
        self.penalty_factor = 10

    def f1(self, x):
        j1 = [j for j in range(1, self.dimension) if j % 2 == 0]
        yj1 = [x[j] - 0.8*x[0]*np.cos(6*np.pi*x[0] + j*np.pi/self.dimension) for j in j1]
        return x[0] + np.sum(np.power(yj1, 2))

    def f2(self, x):
        j2 = [j for j in range(1, self.dimension) if j % 2 != 0]
        yj2 = [x[j] - 0.8*x[0]*np.sin(6*np.pi*x[0] + j*np.pi/self.dimension) for j in j2]
        return np.power(1-x[0], 2) + np.sum(np.power(yj2, 2))

    def c1(self, x):
        c1 = x[1] - 0.8*x[0]*np.sin(6*np.pi*x[0] + 2*np.pi/self.dimension) - np.sign(0.5*(1-x[0]) - np.power(1-x[0], 2)) * \
        np.sqrt(np.abs(0.5 * (1-x[0]) - np.power(1-x[0], 2))) 
        
        if c1>= 0 :
            return 0.0
        else:
            return c1
    
    def c2(self, x):

        c2 = x[3] - 0.8*x[0]*np.sin(6*np.pi*x[0] + 4*np.pi/self.dimension) - np.sign(0.25 * np.sqrt(1-x[0]) - 0.5*(1-x[0])) * \
        np.sqrt(np.abs(0.25 * np.sqrt(1-x[0]) - 0.5*(1-x[0]))) 

        if c2>= 0 :
            return 0.0
        else:
            return c2
    
    def fitness(self, individual):
        return np.array([self.f1(individual), self.f2(individual), - (np.abs(self.c1(individual)) + np.abs(self.c2(individual)))])
    
    def g(self, weight_vector, ref_point, fitness):
        if self.cons_method == 'penalization':
            return np.max([weight_vector[j] * np.abs(fitness[j] - ref_point[j]) for j in range(self.num_functions)]) - \
            self.penalty_factor * fitness[-1]
        else: 
            return np.max([weight_vector[j] * np.abs(fitness[j] - ref_point[j]) for j in range(self.num_functions)])

    
    def create_search_space(self):
        search_space = np.zeros((self.dimension, 2))
        search_space[0][0] = 0
        search_space[0][1] = 1
        for i in range(1, self.dimension):
            search_space[i][0] = -2
            search_space[i][1] = 2
        return search_space
    
    def plot_function(self):
        population = np.zeros((100, self.dimension))
        f1 = np.zeros(100)
        f2 = np.zeros(100)

        for i in range(100):
            for j in range(self.dimension):
                population[i][j] = np.random.uniform(self.search_space[j][0], self.search_space[j][1])
                
            f1[i] = self.f1(population[i])
            f2[i] = self.f2(population[i])
        
        plt.scatter(f1, f2, color='blue', s=1)

    def plot_ideal_front(self):

        f1 = np.linspace(0, 1, 100)
        f2 = np.zeros(100)

        for i, x in enumerate(f1):
            if x <= 0.5:
                f2[i] = np.power(1-x, 2)
            elif x <= 0.75:
                f2[i] = 0.5*(1-x)
            else:
                f2[i] = 0.25 * np.sqrt(1-x)
        
        plt.scatter(f1, f2, color='blue', s=2, label='Ideal Front')



