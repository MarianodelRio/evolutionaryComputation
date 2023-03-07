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

    def f1(self, individual):
        return individual[0]

    def f2(self, individual):
        g = 1 + 9 * np.sum(individual[1:]) / (self.dimension - 1)
        h = 1 - np.sqrt(self.f1(individual) / g) - (self.f1(individual) / g) * np.sin(10 * np.pi * self.f1(individual))
        return g * h

    def fitness(self, individual):
        return np.array([self.f1(individual), self.f2(individual)])
    
    def restrictions(self, individual):
        return False
    
    def create_search_space(self):
        search_space = np.zeros((self.dimension, 2))
        for i in range(self.dimension):
            search_space[i][0] = 0
            search_space[i][1] = 1
        return search_space
    
    def g(self, individual, ref_point):
        return max(self.f1(individual) - ref_point[0], self.f2(individual) - ref_point[1])
    
    def plot_ideal_front(self):

        x = np.concatenate((np.linspace(0, 0.0830015349, 100), np.linspace(0.1822287280, 0.2577623634, 100) ,np.linspace(0.4093136748, 0.4538821041, 100), np.linspace(0.6183967944, 0.6525117038, 100), np.linspace(0.8233317983, 0.8518328654, 100)), axis=0)
        
        f = 1 - np.sqrt(x) - x * np.sin(10 * np.pi * x)


        plt.scatter(x, f, color='blue')
        plt.show()
    

class CF6:

    def __init__(self, dimension):
        self.name = 'CF6'
        self.dimension = dimension
        self.search_space = self.create_search_space()

    def f1(self, x):
        
        pass 

    def f2(self, individual):
        pass

    def create_search_space(self):
        search_space = np.zeros((self.dimension, 2))
        search_space[0][0] = 0
        search_space[0][1] = 1
        for i in range(1, self.dimension):
            search_space[i][0] = -2
            search_space[i][1] = 2
        return search_space
    
    def plot_ideal_front(self):
        pass

