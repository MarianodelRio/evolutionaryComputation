from src.problems import ZDT3
from src.problems import CF6
from src.ev_algorithm import EA


zdt3 = ZDT3(dimension=30)
cf6 = CF6(dimension=30)

problem = cf6
population_size = 40
generations = 1000
dimension = 4
mutation_rate = 0.55
neighborhood_size = 20
SIG = 20
F = 0.5

ea = EA(problem, population_size, \
                 generations, mutation_rate, \
                    neighborhood_size, SIG, F)

ea.run_algorithm()
ea.export_historic(name='zdt3p40g100.out')
