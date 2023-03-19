from trainer import execute
from src.problems import ZDT3, CF6
from stadistics import plot_superposition

def generate_zdt3(pop_size, generations, neighborhood_size, n_ex=10, F=0.5, mutation_rate=0.5, SIG=20):
    dim = 30
    problem = ZDT3(dim)
    
    for i in range(n_ex):
        name_file = 'METRICS/resultados/zdt3/EVAL{}/P{}G{}/zdt3_all_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        name_file2 = 'METRICS/resultados/zdt3/EVAL{}/P{}G{}/zdt3_final_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)

        if (i+1)<10:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/zdt3/EVAL{}/P{}G{}/zdt3_final_popp{}g{}_seed0{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        else:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/zdt3/EVAL{}/P{}G{}/zdt3_final_popp{}g{}_seed099.out'.format(pop_size*generations, pop_size, generations, pop_size, generations)

        execute(problem, pop_size, generations, mutation_rate, neighborhood_size, SIG, F, name_file, name_file2)
        
        plot_superposition(name_file2, name_file_nsgaii, pop_size, generations, problem, i+1)

def generate_cf6_4d(pop_size, generations, neighborhood_size=4, n_ex=10, F=0.5, mutation_rate=0.5, SIG=20):
    dim = 4
    problem = CF6(dim)
    
    for i in range(n_ex):
        name_file = 'METRICS/resultados/cf6_4d/EVAL{}/P{}G{}/cf6_4d_all_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        name_file2 = 'METRICS/resultados/cf6_4d/EVAL{}/P{}G{}/cf6_4d_final_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)

        if (i+1)<10:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/cf6_4d/EVAL{}/P{}G{}/cf6_4d_final_popp{}g{}_seed0{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        else:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/cf6_4d/EVAL{}/P{}G{}/cf6_4d_final_popp{}g{}_seed099.out'.format(pop_size*generations, pop_size, generations, pop_size, generations)

        execute(problem, pop_size, generations, mutation_rate, neighborhood_size, SIG, F, name_file, name_file2)

        plot_superposition(name_file, name_file_nsgaii, pop_size, generations, problem, i+1)

def generate_cf6_16d(pop_size, generations, neighborhood_size=4, n_ex=10, F=0.5, mutation_rate=0.5, SIG=20):
    dim = 16
    problem = CF6(dim)
    
    for i in range(n_ex):
        name_file = 'METRICS/resultados/cf6_16d/EVAL{}/P{}G{}/cf6_16d_all_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        name_file2 = 'METRICS/resultados/cf6_16d/EVAL{}/P{}G{}/cf6_16d_final_p{}g{}_{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)

        if (i+1)<10:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/cf6_16d/EVAL{}/P{}G{}/cf6_16d_final_popp{}g{}_seed0{}.out'.format(pop_size*generations, pop_size, generations, pop_size, generations, i+1)
        else:
            name_file_nsgaii = 'METRICS/resultados_NSGAII/cf6_16d/EVAL{}/P{}G{}/cf6_16d_final_popp{}g{}_seed099.out'.format(pop_size*generations, pop_size, generations, pop_size, generations)

        execute(problem, pop_size, generations, mutation_rate, neighborhood_size, SIG, F, name_file, name_file2)

        plot_superposition(name_file, name_file_nsgaii, pop_size, generations, problem, i+1)

if __name__ == '__main__':
    #generate_zdt3(40, 100, 12)
    #generate_zdt3(80, 50, 24)
    #generate_zdt3(100, 40, 30)
    #generate_zdt3(40, 250, 12)
    #generate_zdt3(100, 100, 30)
    #generate_zdt3(200, 50, 60)
    

    # Penalty factor -> 30
    #generate_cf6_4d(40, 100)
    #generate_cf6_4d(80, 50)
    #generate_cf6_4d(100, 40)
    #generate_cf6_4d(40, 250)
    #generate_cf6_4d(100, 100)
    generate_cf6_4d(200, 50)

    # Penalty factor -> 10
    #generate_cf6_16d(40, 100)
    #generate_cf6_16d(80, 50)
    #generate_cf6_16d(100, 40)
    #generate_cf6_16d(40, 250)
    #generate_cf6_16d(100, 100)
    #generate_cf6_16d(200, 50)