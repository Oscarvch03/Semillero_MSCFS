# LIBRERIAS IMPORTADAS #########################################################
################################################################################

import Graph as Gr

# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

N = 11

# Grafo Completo de la vecindad entre agentes
G1 = Gr.Star_Graph(N)
G1.generate_edges()
print(G1)
G1.generate_txts()
G1.graficar_graph()
