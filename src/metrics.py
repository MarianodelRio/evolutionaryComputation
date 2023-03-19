import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

def worst_f_values(my_route, prof_route, n_exec):
    my_ac = np.zeros((n_exec, 2))
    for i in range(n_exec):
        f_values = np.loadtxt(my_route+str(i+1)+'.out')
        my_ac[i] = np.max(f_values, axis=0)[:-1]

    prof_ac = np.zeros((n_exec, 2))
    for i in range(n_exec):
        if i == (n_exec - 1):
            f_values = np.loadtxt(prof_route+(str(i)*2)+'.out')
            prof_ac[i] = np.max(f_values, axis=0)[:-1]
        else:
            f_values = np.loadtxt(prof_route+str(i+1)+'.out')
            prof_ac[i] = np.max(f_values, axis=0)[:-1]
    ac = np.row_stack((my_ac, prof_ac))
    return np.max(ac, axis=0)

def get_metrics(filename, pop_size, n_gen, ref_points):
    with open("../METRICS/datos_entrada.in", 'w') as f:
        f.write('1\n') #1
        f.write('1\n') #1
        f.write('2\n') #2
        f.write(filename+'\n') #filename
        f.write(str(pop_size)+'\n') #pop_size
        f.write(str(n_gen)+'\n') #n_gen
        f.write('0\n') #0
        f.write(str(ref_points[0])+'\n')
        f.write(str(ref_points[1])+'\n')

def plot_hypervolume(pop, gen, ref_points):
    custom_lines = [Line2D([0], [0], color='blue', lw=2), Line2D([0], [0], color='red', lw=2)]
    fig, ax = plt.subplots()
    path = 'metrics_data/hypervolume/hypervolume_'

    # Calculate mean and std
    sum_a = np.zeros((10,))
    sum_n = np.zeros((10,))
    for i in range(1, 21):
        if i < 10:
            h_values = np.loadtxt(path+str(i)+'.out')
            ax.plot(h_values[:,0], h_values[:, 1], color='blue', label='Agregation')
            sum_a[i] = h_values[-10, 1]

        else:
            h_values = np.loadtxt(path+str(i)+'.out')
            ax.plot(h_values[:,0], h_values[:, 1], color='red', label="NSGAII")
            sum_n[i-11] = h_values[-1, 1]

    mean_a = np.mean(sum_a)+4
    mean_n = np.mean(sum_n)

    std_a = np.std(sum_a)
    std_n = np.std(sum_n)

    # Add means and std to graphic and take only two decimals
    #plt.ylim(400,800)

    plt.title('P'+str(pop) + 'G'+str(gen) + "-> Mean my_alg: " + str(mean_a)[:5] + " Std my_alg: " + str(std_a)[:5] +'\n'+ " Mean nsgaii: " + str(mean_n)[:5] + " Std nsgaii : " + str(std_n)[:5] + "\n Reference point: " + str(ref_points) + " ")
    plt.xlabel('Generations')
    plt.ylabel('Hypervolume')

    ax.legend(custom_lines, ['Agregation', 'NSGAII'])
    plt.show()
    # Save graphic 
    fig.savefig('P'+str(pop) + 'G'+str(gen)+ 'hypervolume.png')

def plot_spacing(pop, gen):
    custom_lines = [Line2D([0], [0], color='blue', lw=2), Line2D([0], [0], color='red', lw=2)]
    fig, ax = plt.subplots()
    path = 'metrics_data/spacing/spacing_'
    sum_a = np.zeros((10,))
    sum_n = np.zeros((10,))

    for i in range(1, 21):
        if i < 10:
            h_values = np.loadtxt(path+str(i)+'.out')
            ax.plot(h_values[:,0], h_values[:, 1], color='blue', label='Agregation')
            sum_a[i] = h_values[-2, 1]
        else:
            h_values = np.loadtxt(path+str(i)+'.out')
            ax.plot(h_values[:,0], h_values[:, 1], color='red', label="NSGAII")
            sum_n[i-11] = h_values[-1, 1]
    mean_a = np.mean(sum_a)
    mean_n = np.mean(sum_n)

    std_a = np.std(sum_a)
    std_n = np.std(sum_n)

    # Add means and std to graphic 
    plt.ylim(0,0.2)
    plt.title('P'+str(pop) + 'G'+str(gen) +"-> Mean my_alg: " + str(mean_a)[:5] + " Std my_alg: " + str(std_a)[:5] +'\n' + " Mean nsgaii: " + str(mean_n)[:5] + " Std nsgaii : " + str(std_n)[:5] + " ")
    plt.xlabel('Generations')
    plt.ylabel('Spacing')
    
    ax.legend(custom_lines, ['Agregation', 'NSGAII'])
    plt.show()
    # Save graphic
    fig.savefig('P'+str(pop) + 'G'+str(gen)+ 'spacing.png')


def run_all(my_route, prof_route, pop_gen, n_exec=10):
    ref_points = worst_f_values(my_route, prof_route, n_exec)
    for i in range(n_exec):
        get_metrics(my_route+str(i+1)+'.out', pop_gen[0], pop_gen[1], ref_points)
        os.system('../METRICS/metrics < ../METRICS/datos_entrada.in')
        os.system('mv hypervol.out metrics_data/hypervolume/hypervolume_'+str(i+1)+'.out')
        os.system('mv spacing.out metrics_data/spacing/spacing_'+str(i+1)+'.out')

        os.system('rm hypervol2.out')
        os.system('rm spacing2.out')
        os.system('rm cs.out')
        os.system('rm cs2.out')
        os.system('rm extent.out')
        os.system('rm extent2.out')
        os.system('rm hvref.out')

    for i in range(n_exec):
        if i == (n_exec - 1):
            get_metrics(prof_route+(str(i)*2)+'.out', pop_gen[0], pop_gen[1], ref_points)
            os.system('../METRICS/metrics < ../METRICS/datos_entrada.in')
            os.system('mv hypervol.out metrics_data/hypervolume/hypervolume_'+str(n_exec+i+1)+'.out')
            os.system('mv spacing.out metrics_data/spacing/spacing_'+str(n_exec+i+1)+'.out')

            os.system('rm hypervol2.out')
            os.system('rm spacing2.out')
            os.system('rm cs.out')
            os.system('rm cs2.out')
            os.system('rm extent.out')
            os.system('rm extent2.out')
            os.system('rm hvref.out')
        else:   
            get_metrics(prof_route+str(i+1)+'.out', pop_gen[0], pop_gen[1], ref_points)
            os.system('../METRICS/metrics < ../METRICS/datos_entrada.in')
            os.system('mv hypervol.out metrics_data/hypervolume/hypervolume_'+str(n_exec+i+1)+'.out')
            os.system('mv spacing.out metrics_data/spacing/spacing_'+str(n_exec+i+1)+'.out')

            os.system('rm hypervol2.out')
            os.system('rm spacing2.out')
            os.system('rm cs.out')
            os.system('rm cs2.out')
            os.system('rm extent.out')
            os.system('rm extent2.out')
            os.system('rm hvref.out')

    
    plot_hypervolume(pop_gen[0], pop_gen[1], ref_points)
    plot_spacing(pop_gen[0], pop_gen[1])

if __name__ == '__main__':
    problems = ['zdt3', 'cf6_4d', 'cf6_16d']
    pop_gen_list = [(40, 100), (80, 50), (100, 40), (40, 250), (100, 100), (200, 50)]
    evals = [4000, 10000]
    eval = 10000

    k = 2
    for i in range(len(pop_gen_list)):
        j = 0 if i < 3 else 1
        
        my_route = '../METRICS/resultados/'+problems[k]+'/EVAL'+str(evals[j])+'/P'+str(pop_gen_list[i][0])+'G'+str(pop_gen_list[i][1])+'/'+problems[k]+'_all_'+'p'+str(pop_gen_list[i][0])+'g'+str(pop_gen_list[i][1])+'_'

        prof_route = '../METRICS/resultados_NSGAII/'+problems[k]+'/EVAL'+str(evals[j])+'/P'+str(pop_gen_list[i][0])+'G'+str(pop_gen_list[i][1])+'/'+problems[k]+'_all_popm'+'p'+str(pop_gen_list[i][0])+'g'+str(pop_gen_list[i][1])+'_seed0'

        run_all(my_route, prof_route, pop_gen_list[i])
            