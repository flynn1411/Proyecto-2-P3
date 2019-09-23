#clase grafo
from vertex import *

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        self.vertices["%s" %(vertex.name)] = vertex

    def addEdge(self, origin, destination, weight):
        self.vertices[str(origin.name)].setEdgeWith(destination.name, weight)

graph = Graph()
graph.addVertex(Vertex("A"))