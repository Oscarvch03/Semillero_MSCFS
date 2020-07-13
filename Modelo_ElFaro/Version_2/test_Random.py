# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Graph as Gr

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 6

# Grafo Completo de la vecindad entre agentes
G1 = Gr.Random_Graph(N, 0.5)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
