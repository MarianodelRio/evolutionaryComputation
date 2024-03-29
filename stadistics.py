'''
Script to get stadistics and comparations of the algorithm implemented and NSGAII

@author: Mariano del Río
@date: 15-03-2023
'''

import numpy as np
from matplotlib import pyplot as plt
import os

def plot_superposition(file_m, file_nsgaii, population_size, generations, problem, n_ex):

    # Read files with numpy 
    data_m = np.loadtxt(file_m)
    data_nsgaii = np.loadtxt(file_nsgaii)

    # Take last generation    
    data_m = data_m[-population_size:]
    data_nsgaii = data_nsgaii[-population_size:]

    # Draw ideal front 
    problem.plot_ideal_front()

    # Draw data 
    plt.xlim(-0.10, 1.1)
    plt.ylim(-2,2)
    plt.xlabel('f1')
    plt.ylabel('f2')
    plt.title(problem.name + ' P'+str(population_size)+' G'+str(generations))
    plt.scatter(data_m[:,0], data_m[:,1], color='red', label='MY_ALGORITHM', s=2)
    plt.scatter(data_nsgaii[:,0], data_nsgaii[:,1], color='black', label='NSGAII', s=2)
    plt.legend()
    # Save graphic 
    plt.savefig('data/'+problem.name+'_'+str(population_size)+'_'+str(generations) + '_' + str(n_ex) +'.png')
    plt.cla()


def main():

    print("HEY")

if __name__ == "__main__":
    main()