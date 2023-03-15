'''
Script to get stadistics and comparations of the algorithm implemented and NSGAII

@author: Mariano del Río
@date: 15-03-2023
'''

import numpy as np
from src.problems import CF6, ZDT3
from matplotlib import pyplot as plt

def plot_superposition(file_m, file_nsgaii, population_size, generations, problem):

    # Read files with numpy 
    data_m = np.loadtxt(file_m, delimiter=' ')
    data_nsgaii = np.loadtxt(file_nsgaii, delimiter=' ')

    # Take last generation    
    data_m = data_m[-population_size:]
    data_nsgaii = data_nsgaii[-population_size:]

    # Draw ideal front 
    problem.plot_ideal_front()

    # Draw data 
    plt.plot(data_m[:,0], data_m[:,1], 'o', color='red', label='MY_ALGORITHM')
    plt.plot(data_nsgaii[:,0], data_nsgaii[:,1], 'o', color='black', label='NSGAII')


def main():

    print("HELLO")

if __name__ == "__main__":
    main()