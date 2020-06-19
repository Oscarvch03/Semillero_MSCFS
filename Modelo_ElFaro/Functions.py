import Class as Cl

import random

def create_agents(N):
    Agents = []
    for i in range(N):
        estr = random.choice([0, 1])
        scr = 0
        pol = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
        Agents.append(Cl.Agent(estr, scr, pol, []))
    return Agents
