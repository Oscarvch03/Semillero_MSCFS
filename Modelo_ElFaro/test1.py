# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl
import Functions as func

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 6
ROUNDS = 2

# Crear politicas
pol0 = Cl.Politica(0)
pol1 = Cl.Politica(1)
pol2 = Cl.Politica(2)
pol3 = Cl.Politica(3)
pol4 = Cl.Politica(4)
pol5 = Cl.Politica(5)
pol6 = Cl.Politica(6)
pol7 = Cl.Politica(7)

# Crear N agentes
Agentes = func.create_agents(N)
# print()
# for i in range(len(Agentes)):
#     print(i)
#     print(Agentes[i])
#     print()

# Grafo regular de la vecindad entre agentes
degree = 3
G1 = Cl.Regular_Graph(N, degree)
G1.generate_edges()
# print(G1.edges)
print(G1)
G1.generate_txts()
G1.graficar_graph()

# Ejecutar las rondas.......................
