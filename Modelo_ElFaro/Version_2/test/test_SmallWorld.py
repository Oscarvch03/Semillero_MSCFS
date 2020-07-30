# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import sys
sys.path.insert(0, "../")
# print(sys.path)
import Graph.Graph as Gr

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 9

# Grafo Completo de la vecindad entre agentes
G1 = Gr.Small_World_Graph(N, 0.)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
