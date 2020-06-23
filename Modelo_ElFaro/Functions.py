# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl

import random

# CLASES Y FUNCIONES ###########################################################
################################################################################

def create_agents(N):
    Agents = []
    for i in range(N):
        estr = random.choice([0, 1])
        scr = 0
        pol = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
        Agents.append(Cl.Agent(estr, scr, pol, []))
    return Agents


def print_agents(agents):
    for i in range(len(agents)):
        print(i)
        print(agents[i])
        print()


def asignar_vecinos(N, agents, graph):
    for i in range(N):
        for j in graph.edges:
            if(j[0] == i):
                agents[i].vecinos.append(j[1])
            elif(j[1] == i):
                agents[i].vecinos.append(j[0])


def calcular_n_t(agents):
    cont = 0
    for i in agents:
        if(i.estrategias[-1] == 1):
            cont += 1
    return cont


def actualizar_puntajes(agents, ro_t, R):
    for i in agents:
        if(i.estrategias[-1] == 0):  # No ir
            i.scores.append(0)
        else:  # Si ir
            if(ro_t <= R):
                i.scores.append(1)
            else:
                i.scores.append(-1)


def puntaje_max(vecinos, agents):
    puntajes = [(i, agents[i].scores[-1]) for i in vecinos]
    max = puntajes[0]
    for i in range(1, len(puntajes)):
        if(puntajes[i][1] > max[1]):
            max = puntajes[i]
    return max


def actualizar_politicas(agents):
    for i in range(len(agents)):
        max = puntaje_max(agents[i].vecinos, agents)
        if(max[1] > agents[i].scores[-1]):
            new_pol = agents[max[0]].politicas[-1]
            agents[i].politicas.append(new_pol)
        else:
            old_pol = agents[i].politicas[-1]
            agents[i].politicas.append(old_pol)


def actualizar_estrategias(agents):
    for i in range(len(agents)):
        st = agents[i].estrategias[-1]
        pt = agents[i].scores[-1]
        num_ult_pol = agents[i].politicas[-1]
        ult_pol = Cl.Politica(num_ult_pol)
        new_st = ult_pol.politica[(st, pt)]
        agents[i].estrategias.append(new_st)


def print_total_scores(agents):
    print("Puntajes Finales: ")
    for i in range(len(agents)):
        print("Agente {0}:".format(i), sum(agents[i].scores))
