from src.problems import ZDT3
from src.problems import CF6
from src.ev_algorithm import EA
import numpy as np


def execute(problem, population_size, generations, mutation_rate, neighborhood_size, SIG, F, name_file, name_file2):
   
   ea = EA(problem, population_size, \
                  generations, mutation_rate, \
                     neighborhood_size, SIG, F)

   ea.run_algorithm()
   ea.export_historic(name=name_file)
   ea.export_historic_final(name=name_file2)


def main():

   # ZDT3
   print("ZDT3")

if __name__ == "__main__":
   main()