from src.problems import ZDT3
from src.problems import CF6
from src.ev_algorithm import EA
import numpy as np

import subprocess


population_size = 40
generations = 100
dim = 4
mutation_rate = 0.55
neighborhood_size = 20
SIG = 20
F = 0.5

zdt3 = ZDT3(dimension=dim)
cf6 = CF6(dimension=dim)

problem = zdt3

ea = EA(problem, population_size, \
                 generations, mutation_rate, \
                    neighborhood_size, SIG, F)

#ea.run_algorithm()
#print(np.max(ea.historic, axis=0))
#ea.export_historic(name='m_zdt3p40g100.out')

# Use subprocess to execute a command and get its output

cmd = 'ls' 

subprocess.call(cmd, shell=True)
