# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Class as Cl

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 6

# Grafo Completo de la vecindad entre agentes
G1 = Cl.Random_Graph(N)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
