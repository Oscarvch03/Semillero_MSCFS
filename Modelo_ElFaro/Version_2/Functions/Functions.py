# LIBRERIAS IMPORTADAS #########################################################
################################################################################
import sys
sys.path.insert(0, "../")
# print(sys.path)

import Class.Class as Cl
import Graph.Graph as Gr

import random
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import os.path

# CLASES Y FUNCIONES ###########################################################
################################################################################


def create_agents(N, graph, R):
    Agents = []
    for i in range(N):
        # print("crea {0}".format(i))
        estr = random.choice([0, 1])
        # scr = random.choice([-1, 0, 1])
        pol = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
        Agents.append(Cl.Agent(estr, None, pol, []))
    asignar_vecinos(N, Agents, graph)
    n_t = calcular_n_t(Agents)
    ro_t = n_t / N
    actualizar_puntajes(Agents, ro_t, R)
    return Agents


def asignar_vecinos(N, agents, graph):
    for i in range(N):
        for j in graph.edges:
            if(j[0] == i):
                agents[i].vecinos.append(j[1])
            elif(j[1] == i):
                agents[i].vecinos.append(j[0])


def actualizar_puntajes(agents, ro_t, R):
    for i in agents:
        if(i.actual_est == 0):  # No ir
            i.actual_scr = 0
        else:  # Si ir
            if(ro_t <= R):
                i.actual_scr = 1
            else:
                i.actual_scr = -1


def print_agents(agents):
    for i in range(len(agents)):
        print(i)
        print(agents[i])
        print()


def print_file(agents, ROUND, ID_simulation):
    char = 'w' if ROUND == 0 else 'a'

    save_path = '/home/osvch03/Desktop/Semillero_MSCFS/Modelo_ElFaro/Version_2/results'
    name1 = os.path.join(save_path, 'estrategias_{0}.csv'.format(ID_simulation))
    name2 = os.path.join(save_path, 'politicas_{0}.csv'.format(ID_simulation))
    name3 = os.path.join(save_path, 'puntajes_{0}.csv'.format(ID_simulation))

    file1 = open(name1, char)
    file2 = open(name2, char)
    file3 = open(name3, char)

    if(ROUND == 0):
        file1.write("ROUND" + ",")
        file2.write("ROUND" + ",")
        file3.write("ROUND" + ",")
        for i in range(len(agents)):
            file1.write("A{0}".format(i) + ",")
            file2.write("A{0}".format(i) + ",")
            file3.write("A{0}".format(i) + ",")
        file1.write("\n")
        file2.write("\n")
        file3.write("\n")

    file1.write(str(ROUND) + ",")
    file2.write(str(ROUND) + ",")
    file3.write(str(ROUND) + ",")

    for i in agents:
        file1.write(str(i.actual_est) + ",")
        file2.write(str(i.actual_pol) + ",")
        file3.write(str(i.actual_scr) + ",")

    file1.write("\n")
    file2.write("\n")
    file3.write("\n")

    file1.close()
    file2.close()
    file3.close()


def calcular_n_t(agents):
    cont = 0
    for i in agents:
        if(i.actual_est == 1):
            cont += 1
    return cont


def puntaje_max(vecinos, agents):
    puntajes = [(i, agents[i].actual_scr) for i in vecinos]
    if(len(puntajes) != 0):
        max = puntajes[0]
        for i in range(1, len(puntajes)):
            if(puntajes[i][1] > max[1]):
                max = puntajes[i]
        maxs = []
        for j in puntajes:
            if(j[1] == max[1]):
                maxs.append(j)
        return(random.choice(maxs))
    else:
        return 2 # No adopta ninguno


def actualizar_politicas(agents):
    for i in range(len(agents)):
        max = puntaje_max(agents[i].vecinos, agents)
        if(max == 2):
            old = agents[i].actual_pol
            agents[i].new_pol = old
        else:
            if(max[1] > agents[i].actual_scr):
                # new_pol = old_pols[max[0]]
                # agents[i].politicas.append(new_pol)
                new = agents[max[0]].actual_pol
                agents[i].new_pol = new
            else:
                # old_pol = agents[i].politicas[-1]
                # agents[i].politicas.append(old_pol)
                old = agents[i].actual_pol
                agents[i].new_pol = old

    for j in range(len(agents)):
        agents[j].actual_pol = agents[j].new_pol


def actualizar_estrategias(agents):
    for i in range(len(agents)):
        # st = agents[i].estrategias[-1]
        # pt = agents[i].scores[-1]
        # num_ult_pol = agents[i].politicas[-1]
        # ult_pol = Cl.Politica(num_ult_pol)
        # new_st = ult_pol.politica[(st, pt)]
        # agents[i].estrategias.append(new_st)
        st = agents[i].actual_est
        pt = agents[i].actual_scr
        num_ult_pol = agents[i].actual_pol
        ult_pol = Cl.Politica(num_ult_pol)
        new_st = ult_pol.politica[(st, pt)]
        agents[i].actual_est = new_st


def simulation(ROUNDS, N, agents, R, k, ID_simulation):
    opt_assist = []
    tot_reward = []
    # Terminar
    print_file(agents, 0, ID_simulation)
    for i in range(1, ROUNDS + 1):
        # print()
        # print("RONDA {0}".format(i+1))
        # print()
        n_t = calcular_n_t(agents)
        ro_t = n_t / N  # Proporcion de asistencia
        actualizar_puntajes(agents, ro_t, R)
        # old_pols = [i.politicas[-1] for i in agents]
        # actualizar_politicas(agents, old_pols)
        actualizar_politicas(agents)
        actualizar_estrategias(agents)
        if(i % k == 0):
            print_file(agents, i, ID_simulation)


def results(N, R, graph, rounds, time, k, ID_simulation):
    result = open('results.dat', 'a')
    result.write("\n")
    result.write("Simulation: {0}\n".format(ID_simulation))
    result.write("Red: {0}\n".format(graph.name))
    result.write("Agentes: {0}\n".format(N))
    result.write("Umbral: {0}\n".format(R))
    result.write("Rondas: {0}\n".format(rounds))
    result.write("k: {0}\n".format(k))
    result.write("Time: {0}\n".format(time))
    result.write("Out: estrategias_{0}.csv, politicas_{0}.csv, puntajes_{0}.csv, graf_{0}.png\n".format(ID_simulation))
    result.write("\n")
    result.close()


def graficar(N, R, rounds, l, ID_simulation, see):

    rondas = [i for i in range(0, rounds + 1, l)]
    # print(rondas)

    save_path = '/home/osvch03/Desktop/Semillero_MSCFS/Modelo_ElFaro/Version_2/results'
    name1 = os.path.join(save_path, 'estrategias_{0}.csv'.format(ID_simulation))
    name2 = os.path.join(save_path, 'politicas_{0}.csv'.format(ID_simulation))
    name3 = os.path.join(save_path, 'puntajes_{0}.csv'.format(ID_simulation))

    estrategias = pd.read_csv(name1)
    asist = []
    for i in estrategias.itertuples():
        aux = [i[j] for j in range(2, len(i) - 1)]
        asist.append(sum(aux))
    asistencia = [i/N for i in asist]


    politicas = pd.read_csv(name2)
    pol0 = []
    pol1 = []
    pol2 = []
    pol3 = []
    pol4 = []
    pol5 = []
    pol6 = []
    pol7 = []
    for i in politicas.itertuples():
        cont = [0, 0, 0, 0, 0, 0, 0, 0]
        for k in range(2, len(i) - 1):
            if i[k] == 0:
                cont[0] += 1
            elif i[k] == 1:
                cont[1] += 1
            elif i[k] == 2:
                cont[2] += 1
            elif i[k] == 3:
                cont[3] += 1
            elif i[k] == 4:
                cont[4] += 1
            elif i[k] == 5:
                cont[5] += 1
            elif i[k] == 6:
                cont[6] += 1
            elif i[k] == 7:
                cont[7] += 1
        pol0.append(cont[0])
        pol1.append(cont[1])
        pol2.append(cont[2])
        pol3.append(cont[3])
        pol4.append(cont[4])
        pol5.append(cont[5])
        pol6.append(cont[6])
        pol7.append(cont[7])


    puntajes = pd.read_csv(name3)
    scr = []
    for i in puntajes.itertuples():
        aux = [i[j] for j in range(2, len(i) - 1)]
        scr.append(sum(aux))
    scores = [i/N for i in scr]


    fig, ax = plt.subplots(2, 2)

    ax[0, 0].plot(rondas, asistencia, 'g')
    ax[0, 0].set(ylabel='Asistencia(%)', xlim = [0, rounds], ylim = [0, 1],
       title='Asistencia por Ronda a El Farol')
    # ax[0].legend(["Asistencia por Ronda"])
    ax[0, 0].grid()

    ax[0, 1].plot(rondas, pol0)
    ax[0, 1].plot(rondas, pol1)
    ax[0, 1].plot(rondas, pol2)
    ax[0, 1].plot(rondas, pol3)
    ax[0, 1].plot(rondas, pol4)
    ax[0, 1].plot(rondas, pol5)
    ax[0, 1].plot(rondas, pol6)
    ax[0, 1].plot(rondas, pol7)
    ax[0, 1].set(ylabel='Politicas(# Uso)', xlim = [0, rounds], ylim = [0, N],
       title='Uso de Politicas por Ronda')
    ax[0, 1].legend(["Politica 0", "Politica 1", "Politica 2", "Politica 3", "Politica 4",
               "Politica 5", "Politica 6", "Politica 7"])
    ax[0, 1].grid()

    ax[1, 0].plot(rondas, scores, 'r')
    ax[1, 0].set(xlabel='Rondas', ylabel='Puntaje Promedio', xlim = [0, rounds], ylim = [-1, 1],
       title='Puntaje Promedio por Ronda para cada Agente')
    ax[1, 0].grid()

    ax[1, 1].axis('off')
    ax[1, 1].set(xlim = [0, rounds], ylim = [0, 1])
    ax[1, 1].text(rounds / 2, 0.5,
                  'Graficas El Farol con Parametros:\n Red: {0}\n Agentes = {1}\n Umbral = {2}\n Rondas = {3}\n k = {4}'.format(ID_simulation, N, R, rounds, l),
                  horizontalalignment='center',
                  verticalalignment='center',
                  fontsize = 20)

    fig.set_size_inches(15, 10)
    save_path = '/home/osvch03/Desktop/Semillero_MSCFS/Modelo_ElFaro/Version_2/graphics'
    name = os.path.join(save_path, 'graf_{0}.PNG'.format(ID_simulation))
    plt.savefig(name)
    if see:
        plt.show()
