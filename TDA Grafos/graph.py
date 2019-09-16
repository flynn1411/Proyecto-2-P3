#clase grafo
from vertex import *

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        self.vertices["%s" %(vertex.name)] = vertex

    def addEdge(self, origin, destination, weight):
        if(isinstance(origin, Vertex) and isinstance(destination, Vertex)):
            self.addEdgeInner(origin, destination, weight)
        

    def addEdgeInner(self, origin, destination, weight):
        self.vertices[str(origin.name)].setEdgeWith(destination.name, weight)