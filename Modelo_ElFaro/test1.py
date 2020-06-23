# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl
import Functions as Func

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

# PARAMETROS DEL MODELO
N = 50
R = 0.5
ROUNDS = 100

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

# Crear N agentes
Agentes = Func.create_agents(N)

# Grafo Completo de la vecindad entre agentes
G1 = Cl.Complete_Graph(N)
G1.generate_edges()
print(G1)

# Generar txts
G1.generate_txts()

# Graficar red
# G1.graficar_graph()

# Asignar Vecinos a los agentes
Func.asignar_vecinos(N, Agentes, G1)
# Func.print_agents(Agentes)

# EJECUTAR LAS RONDAS
for i in range(ROUNDS):
    n_t = Func.calcular_n_t(Agentes)
    # print("n_t =", n_t)
    ro_t = n_t / N
    # print("ro_t =", ro_t)
    Func.actualizar_puntajes(Agentes, ro_t, R)
    Func.actualizar_politicas(Agentes)
    Func.actualizar_estrategias(Agentes)
# Func.print_agents(Agentes)
Func.print_total_scores(Agentes)
