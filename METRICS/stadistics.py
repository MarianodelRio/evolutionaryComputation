'''
Script to get stadistics and comparations of the algorithm implemented and NSGAII

@author: Mariano del Río
@date: 15-03-2023
'''

import numpy as np
from matplotlib import pyplot as plt
import os

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


def calculate_max_f1_f2(path1, path2):
    # Calculate of 20 ejecutions max f1 and f2
    max_f1 = 0
    max_f2 = 0
    for i in range(1,11):
        if i <10:
            end = '0'+str(i) + '.out'
        else:
            end = '099' + '.out'

        data1 = np.loadtxt(path1+end)
        data2 = np.loadtxt(path2+end)

        max_f1 = max(max_f1, np.max(data1[:,0]))
        max_f2 = max(max_f2, np.max(data1[:,1]))

        max_f1 = max(max_f1, np.max(data2[:,0]))
        max_f2 = max(max_f2, np.max(data2[:,1]))       
    
    return max_f1, max_f2

def calculate_graphics():

    
    eval_problem = 'EVAL4000_cf64d'
    pop_gen = 'P40G100'
    pop_gen_s = pop_gen.split('G')
    pop = pop_gen_s[0][1:]
    gen = pop_gen_s[1]
    name = 'cf6_4d_all_popmp40g100_seed'
    path1 = 'data/AG/'+eval_problem+'/'+pop_gen + '/'
    path2 = 'data/NSGAII/'+eval_problem+'/'+pop_gen + '/'

    # Calculate max 
    max_f1, max_f2 = calculate_max_f1_f2(path1+name, path2+name)

   
    for i in range(1,2):
        if i <10:
            end = '0'+str(i) 
        else:
            end = '099' 

         # Generate file .in to compare solution 
        file_ag = 'AG_' + eval_problem+'_'+pop_gen + '_' + end +'.in'
        file_nsgaii = 'NSGAII_' + eval_problem+'_'+pop_gen+'_' + end +'.in'

        # Modificate file 
        with open(file_ag, "w") as f:
            f.write('1\n') # Number of exacutions to compare
            f.write('1\n') # All generations
            f.write('2\n') # Number of objectives
            f.write(path1 + end + '.out' + '\n') # Name of file 
            f.write(pop+'\n') # Population size 
            f.write(gen+'\n') # Generations 
            f.write('0\n') # Calculate ref point manual
            f.write(str(max_f1)+ '\n') # Coordinate x of ref point
            f.write(str(max_f2)+ '\n') # Coordinate y of ref point
        
        # Execute command to compare solution
        cmd = './metrics < ' + file_ag
        print(cmd)
        os.system('./metrics < ' + file_ag)

        # Move hipervol, spacing and coverage file to folder data with os commands
        os.system("mv hipervol.out " + path1 + "hipervol_" + str(1) + ".out")
        os.system("mv spacing.out " + path1 + "spacing_" + str(1) + ".out")

        # Modificate file 
        with open(file_nsgaii, "w") as f:
            f.write('1\n') # Number of exacutions to compare
            f.write('1\n') # All generations
            f.write('2\n') # Number of objectives
            f.write(path2 + end + '.out' + '\n') # Name of file 
            f.write(pop+'\n') # Population size 
            f.write(gen+'100\n') # Generations 
            f.write('0\n') # Calculate ref point manual
            f.write(str(max_f1)) # Coordinate x of ref point
            f.write(str(max_f2)) # Coordinate y of ref point
        
        # Execute command to compare solution
        os.system('./metrics < '+file_nsgaii)

        # Move hipervol, spacing and coverage file to folder data with os commands
        os.system("mv hipervol.out " + path1 + "hipervol_" + str(1) + ".out")
        os.system("mv spacing.out " + path1 + "spacing_" + str(1) + ".out")

    

def main():

    calculate_graphics()

if __name__ == "__main__":
    main()