# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl
import Graph as Gr

import random

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


def print_file(agents, ROUND, ini):
    char = 'w' if ROUND == 0 else 'a'

    file1 = open('estrategias.csv', char)
    file2 = open('puntajes.csv', char)
    file3 = open('politicas.csv', char)

    if(ini):
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
        file2.write(str(i.actual_scr) + ",")
        file3.write(str(i.actual_pol) + ",")

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
    max = puntajes[0]
    for i in range(1, len(puntajes)):
        if(puntajes[i][1] > max[1]):
            max = puntajes[i]
    maxs = []
    for j in puntajes:
        if(j[1] == max[1]):
            maxs.append(j)
    return(random.choice(maxs))


def actualizar_politicas(agents):
    for i in range(len(agents)):
        max = puntaje_max(agents[i].vecinos, agents)
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


def simulation(ROUNDS, N, agents, R):
    print_file(agents, 0, True)
    for i in range(ROUNDS):
        # print()
        # print("RONDA {0}".format(i+1))
        # print()
        n_t = calcular_n_t(agents)
        ro_t = n_t / N
        actualizar_puntajes(agents, ro_t, R)
        # old_pols = [i.politicas[-1] for i in agents]
        # actualizar_politicas(agents, old_pols)
        actualizar_politicas(agents)
        actualizar_estrategias(agents)
        print_file(agents, i+1, False)



# def print_total_scores(agents):
#     print("Puntajes Finales: ")
#     for i in range(len(agents)):
#         print("Agente {0}:".format(i), sum(agents[i].scores))
