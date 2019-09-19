# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

class vertex:
    def __init__(self,vertexName):
        self.name = vertexName
        G.add_node("%s" % vertexName)
        self.edge = {}

    def setEgde(self,newVertex):
        self.edge["%s " % (newVertex)] = None
        G.add_node("%s"% newVertex)
        print("Las aristas de %s son %s" %(self.name,self.edge))

    def getEdges(self):
        return [{str(key):{value: None}} for key,value in self.edge.items()]

    def Map(self):
        nx.draw(G, with_labels = True)
        plt.savefig("wea.jpg")
        plt.show()

vertice = vertex("A")
vertice.setEgde("B")
vertice.setEgde("C")
vertice.setEgde("D")
vertice.Map()
print("%s %s" % (vertice.name,vertice.getEdges()))
