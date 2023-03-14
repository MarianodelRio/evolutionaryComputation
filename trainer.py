from src.problems import ZDT3
from src.problems import CF6
from src.ev_algorithm import EA
import numpy as np

import subprocess

def execute(population_size, generations, dim, mutation_rate, neighborhood_size, SIG, F, problem, name_file):
   
   if problem == 'zdt3':
      problem = ZDT3(dimension=dim)
   elif problem == 'cf6':
      problem = CF6(dimension=dim)
   else:
      print("Incorrect choice of problem. Please choose between 'zdt3' and 'cf6'.")
      return

   ea = EA(problem, population_size, \
                  generations, mutation_rate, \
                     neighborhood_size, SIG, F)

   ea.run_algorithm()
   ea.export_historic(name=name_file)

# Use subprocess to execute a command and get its output

#cmd = 'ls' 

#subprocess.call(cmd, shell=True)


def run_zdt3():
   # Executions to solve zdt3 problem in 4000 and 10000 evaluations
   population_size = [40, 80, 100, 40, 100, 200] 
   generations = [100, 50, 40, 250, 100, 50]
   dim = 30
   mutation_rate = 0.8
   neighborhood_size = 10
   SIG = 20
   F = 0.5
   problem = 'zdt3'
   name_file = ['data/AG/m_zdt3p40g100.out', 'data/AG/m_zdt3p80g50.out', 'data/AG/m_zdt3p100g40.out', 
                'data/AG/m_zdt3p40g250.out', 'data/AG/m_zdt3p100g100.out', 'data/AG/m_zdt3p200g50.out']

   for i in range(6):
      execute(population_size[i], generations[i], dim, 
              mutation_rate, neighborhood_size, SIG, F, problem, name_file[i])
      

def run_cf6():
   # Executions to solve cf6 problem in 4000 and 10000 evaluations
   # in 4 and 16 dimensions
   population_size = [40, 80, 100, 40, 100, 200] 
   generations = [100, 50, 40, 250, 100, 50]
   dim = [4,16]
   mutation_rate = 0.8
   neighborhood_size = 10
   SIG = 20
   F = 0.5
   problem = 'cf6'
   name_file1 = ['data/AG/m_cf64dp40g100.out', 'data/AG/m_cf64dp80g50.out', 'data/AG/m_cf64dp100g40.out', 
                'data/AG/m_cf64dp40g250.out', 'data/AG/m_cf64dp100g100.out', 'data/AG/m_cf64dp200g50.out']
   name_file2 = ['data/AG/m_cf616dp40g100.out', 'data/AG/m_cf616dp80g50.out', 'data/AG/m_cf616dp100g40.out', 
                'data/AG/m_cf616dp40g250.out', 'data/AG/m_cf616dp100g100.out', 'data/AG/m_cf616dp200g50.out']

   for i in range(6):
      execute(population_size[i], generations[i], dim[0], 
              mutation_rate, neighborhood_size, SIG, F, problem, name_file1[i])
   
   for i in range(6):
      execute(population_size[i], generations[i], dim[1], 
              mutation_rate, neighborhood_size, SIG, F, problem, name_file2[i])
      
def main():

   run_zdt3()
   run_cf6()

if __name__ == "__main__":
   main()