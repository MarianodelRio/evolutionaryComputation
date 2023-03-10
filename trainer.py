from src.problems import ZDT3
from src.ev_algorithm import EA


zdt3 = ZDT3(dimension=30)
#zdt3.plot_function()

problem = zdt3
population_size = 80
generations = 1000
dimension = 30
mutation_rate = 0.7
neighborhood_size = 20
SIG = 20
F = 0.5

ea = EA(problem, population_size, \
                 generations, mutation_rate, \
                    neighborhood_size, SIG, F)

ea.run_algorithm()
