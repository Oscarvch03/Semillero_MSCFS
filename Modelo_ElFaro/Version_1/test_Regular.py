# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 6

# Grafo Regular de la vecindad entre agentes
degree = 3
G1 = Cl.Regular_Graph(N, degree)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
