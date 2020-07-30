# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import sys
sys.path.insert(0, "../")
# print(sys.path)
import Graph.Graph as Gr

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 6

# Grafo Regular de la vecindad entre agentes
degree = 3
G1 = Gr.Regular_Graph(N, degree)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
