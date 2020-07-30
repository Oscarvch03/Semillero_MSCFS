# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import sys
sys.path.insert(0, "../")
# print(sys.path)
import Graph.Graph as Gr

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 10

# Grafo Completo de la vecindad entre agentes
G1 = Gr.Complete_Graph(N)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
