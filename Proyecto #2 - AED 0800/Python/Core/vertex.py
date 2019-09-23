#-*-coding: utf-8 -*-

#clase Vertice

class Vertex:
    def __init__(self, vertexName):
        #Cada objeto vertice contiene su nombre y un diccionario con sus aristas
        self.name = vertexName
        self.edges = {}

    def setEdgeWith(self, newVertex, weight = 0):
        #Se agrega una arista en el diccionario JSON al usar el nombre del vertice 
        #al otro extremo como llave y el peso como valor. El peso se define con una
        #formula al cargar el grafo desde el archivo de texto plano para poder mostrarlo
        #con mayor facilidad en la interfaz
        self.edges[ "%s" %(newVertex) ] = weight

    def getEdges(self):
        #Se retornan las aristas como un arreglo de diccionarios de la siguiente manera:
        # {vertice: {peso: valor} }, esto asegura un mejor acceso a las aristas de dicho vertice
        return [{str(key) : { "weight": value}} for key, value in self.edges.items()]