# LIBRERIAS IMPORTADAS #########################################################
################################################################################

from numpy import random
import sys

import networkx as nx
import matplotlib.pyplot as plt
import pylab

# CLASES Y FUNCIONES ###########################################################
################################################################################

class Agent:

    def __init__(self, estrategia, score, politica, vecinos):
        # (estrategia inicial, puntaje inicial, politica inicial, lista de vecinos)
        self.estrategias = [estrategia]
        self.scores = [score]
        self.politicas = [politica]
        self.vecinos = vecinos


    def __str__(self):
        msg = "Agent With: \n"
        msg += "E: {0} \n".format(self.estrategias)
        msg += "S: {0} \n".format(self.scores)
        msg += "P: {0} \n".format(self.politicas)
        msg += "V: {0}".format(self.vecinos)
        return msg

################################################################################

class Politica:

    def __init__(self, num_politica): # num_politica = 0, 1, 2, ..., 7
        self.num_politica = num_politica
        self.politica = None

        if(num_politica == 0):
            pol = {(0, 0): 0, (1, 1): 0, (1, -1): 0}
        elif(num_politica == 1):
            pol = {(0, 0): 0, (1, 1): 0, (1, -1): 1}
        elif(num_politica == 2):
            pol = {(0, 0): 0, (1, 1): 1, (1, -1): 0}
        elif(num_politica == 3):
            pol = {(0, 0): 0, (1, 1): 1, (1, -1): 1}
        elif(num_politica == 4):
            pol = {(0, 0): 1, (1, 1): 0, (1, -1): 0}
        elif(num_politica == 5):
            pol = {(0, 0): 1, (1, 1): 0, (1, -1): 1}
        elif(num_politica == 6):
            pol = {(0, 0): 1, (1, 1): 1, (1, -1): 0}
        elif(num_politica == 7):
            pol = {(0, 0): 1, (1, 1): 1, (1, -1): 1}
        else:
            print("The politic is a number in [0, 7]. ")

        self.politica = pol


    def __str__(self):
        msg = "Politic {0} \n".format(self.num_politica)
        msg += "(0, 0): {0} \n".format(self.politica[(0, 0)])
        msg += "(1, 1): {0} \n".format(self.politica[(1, 1)])
        msg += "(1, -1): {0}".format(self.politica[(1, -1)])
        return msg

################################################################################

class Graph:

    def __init__(self, n_nodes):
        self.name = None
        self.n_nodes = n_nodes
        self.n_edges = 0
        self.nodes = []
        self.edges = []


    def __str__(self):
        msg = "We have a {0} graph with {1} nodes and {2} edges. ".format(self.name,
                                                                   self.n_nodes,
                                                                   self.n_edges)
        return msg


    def graficar_graph(self):
        G = nx.Graph()  # Graph
        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.edges)
        # print(G.edges)
        fig = pylab.figure()
        if(len(G.nodes) == self.n_nodes):
            # print("Vamos Bien")
            nx.draw_shell(G, nlist = [range(0, len(G.nodes))], with_labels = True)
            fig.canvas.draw()
            pylab.draw()
        pylab.show()
        plt.show()


################################################################################

def bridge(i, llinks, lnkcnt):
    test = False
    while not test:
        rnd = random.randint(0,len(llinks))
        a = llinks[rnd][0]
        b = llinks[rnd][1]
        pair1 = [min(i,a),max(i,a)]
        pair2 = [min(i,b),max(i,b)]
        if ((a != i) and (b != i)) and ((pair1 not in llinks) and (pair2 not in llinks)):
            llinks.remove([a,b]) # Remove a bond
            llinks.append(pair1) # Add two new bonds
            llinks.append(pair2)
            lnkcnt[i] += 2
            test = True


class Regular_Graph(Graph):

    def __init__(self, n_nodes, degree):
        Graph.__init__(self, n_nodes)
        self.name = "{0}-Regular".format(degree)
        self.n_nodes = n_nodes
        self.degree = degree

        self.aux = []


    def __str__(self):
        return Graph.__str__(self)


    def generate_edges(self):
        ml = self.n_nodes * (self.n_nodes - 1) / 2  # Max number of edges
        tl = self.n_nodes * self.degree / 2  # Theoric number of edges

        lnkcnt = [0 for i in range(self.n_nodes)]  # Edges counter
        llinks = []  # Edges list
        nodes = [i for i in range(self.n_nodes)] # Nodes list
        self.nodes = nodes[:]

        if(tl <= ml):
            self.n_edges = int(tl)

            count = 0
            while(len(nodes) > 0):
                rnd1 = random.randint(0, len(nodes))
                rnd2 = random.randint(0, len(nodes))
                i = nodes[rnd1]
                j = nodes[rnd2]
                if(i != j):
                    if(lnkcnt[i] < self.degree) and (lnkcnt[j] < self.degree):
                        pair = [min(i, j), max(i, j)]
                        if pair not in llinks:
                            count = 0
                            lnkcnt[i] += 1
                            lnkcnt[j] += 1
                            llinks.append(pair)
                            if(lnkcnt[i] == self.degree): nodes.remove(i)
                            if(lnkcnt[j] == self.degree): nodes.remove(j)
                        else:
                            count += 1

                    if(count > len(nodes) * len(nodes)):
                        count1 = 0
                        for n in range(0, len(nodes) - 1):
                            a = nodes[n]
                            for m in range(n + 1, len(nodes)):
                                b = nodes[m]
                                pairv = [min(a, b), max(a, b)]
                                if pairv in llinks: count1 += 1
                        tot = len(nodes) * (len(nodes) - 1) / 2

                        if(count1 == tot):
                            if(lnkcnt[i] < self.degree - 1):  # Make a bridge
                                bridge(i, llinks, lnkcnt)
                            else:
                                nodes.remove(i)

                            if(lnkcnt[j] < self.degree - 1):  # Make a bridge
                                bridge(j, llinks, lnkcnt)
                            else:
                                nodes.remove(j)

                elif(len(nodes) == 1):
                    last = nodes[0]
                    if(lnkcnt[last] < self.degree - 1):  # Make a bridge
                        bridge(last, llinks, lnkcnt)
                    else:
                        nodes.remove(last)

            # print("lnkcnt = ", lnkcnt)
            for i in lnkcnt:
                if(i != self.degree):
                    print("No es regular. ")
                    break

            self.edges = llinks[:]
            self.aux = lnkcnt[:]

        else:
            print("The connectivity degree is too high. ")


    def generate_txts(self):

        # List of edges
        ff = open("edges_list.dat", "w")
        for i in range(len(self.edges)):
            ff.write(str(self.edges[i][0]) + " " + str(self.edges[i][1]) + "\n")
        ff.close()

        # Histogram of degrees
        hist = [0 for i in range(self.n_nodes)]
        for i in self.aux:
            hist[i] += 1

        hf = open("deg_hist.dat", "w")
        for i in range(self.n_nodes):
            hf.write(str(i) + " " + str(hist[i]) + "\n")
        hf.close()

        print("Graph ready. ")


################################################################################

# class Complete_Graph(Graph):

################################################################################


# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
################################################################################

if(__name__ == "__main__"):

    G1 = Regular_Graph(6, 3)
    G1.generate_edges()
    print(G1)
    G1.generate_txts()
    G1.graficar_graph()