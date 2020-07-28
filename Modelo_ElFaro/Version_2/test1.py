# LIBRERIAS IMPORTADAS #########################################################
################################################################################

# print("Importando...")

import Class as Cl
import Functions as Func
import Graph as Gr

import time


# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

# PARAMETROS DEL MODELO
N = 100
R = 0.5
ROUNDS = 300

# Crear politicas (Por si acaso)
pol0 = Cl.Politica(0)
pol1 = Cl.Politica(1)
pol2 = Cl.Politica(2)
pol3 = Cl.Politica(3)
pol4 = Cl.Politica(4)
pol5 = Cl.Politica(5)
pol6 = Cl.Politica(6)
pol7 = Cl.Politica(7)

# Lista de Politicas
pols = [pol0, pol1, pol2, pol3, pol4, pol5, pol6, pol7]
# for i in pols:
#     print(i)

# print("Pols listas")

# Grafo de la vecindad entre agentes
# G1 = Gr.Complete_Graph(N)
# G1 = Gr.Regular_Graph(N, 2)
# G1 = Gr.Scale_Free_Graph() # Aun no
# p = 0.5
# G1 = Gr.Small_World_Graph(N, p)
# G1 = Gr.Ring_Graph(N)
# G1 = Gr.Star_Graph(N)
# G1 = Gr.Wheel_Graph(N, 2)
p = 0.1
G1 = Gr.Random_Graph(N, p)
G1.generate_edges()
# print(G1)


# Generar txts
G1.generate_txts()


# Crear N agentes
Agentes = Func.create_agents(N, G1, R)


ID_simulation = G1.name
k = 5  # Cada k rondas se graba en los csv
# EJECUTAR LAS RONDAS
t_start = time.time()
Func.simulation(ROUNDS, N, Agentes, R, k, ID_simulation)
t_stop = time.time()
time = t_stop - t_start
Func.results(N, R, G1, ROUNDS, time, k, ID_simulation)


# # Graficar red
# G1.graficar_graph()


print("Red:", G1)
print("Agentes:", N)
print("Umbral:", R)
print("Rondas:", ROUNDS)
print("k =", k)
print("Time:", t_stop - t_start)


# Graficar csv
Func.graficar(N, R, ROUNDS, k, ID_simulation, True)

################################################################################

# PARAMETROS
# N = 100
# ROUNDS 300

# Formulas
# Asistencia Optima: 1 - 2*sum(sqrt((ro_t - 0.5)**2) / i)) i es la ronda
# Recompensa Total: suma_puntajes / (ROUNDS * N)

# Simulaciones
# Random con diferente p

## REVISAR CORRECTO FUNCIONAMIENTO
