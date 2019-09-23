
import math
#############################################################################################################

def getTrust(mediumType, distance):
    trustworthiness = 1
    trust = 0.00

    if(mediumType == "CAT5"):
        if (distance >= 50):
            n = math.floor(distance/50)
            trust = 0.0002*n

    elif(mediumType == "CAT6"):
        if (distance >= 50):
            n = math.floor(distance/50)
            trust = 0.0001*n

    elif(mediumType == "Fibra"):
        if (distance >= 100):
            n = math.floor(distance/100)
            trust = 0.0005*n

    elif(mediumType == "WIFI"):
        if (distance >= 6):
            n = math.floor(distance/6)
            trust = 0.006*n

    elif(mediumType == "Coaxial"):
        if (distance >= 100):
            n = math.floor(distance/100)
            trust = 0.0004*n

    else:
        if(distance >= 100):
            n = math.floor(distance/100)
            trust = 0.0001*n

    return (float(trustworthiness) - trustworthiness*trust)


def getWeight(distance, bandwidth, users, traffic, medium):

    return round( ((bandwidth/getTrust(medium, distance) - bandwidth)*(users*traffic)) , 2)
###################################################################################################
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
###################################################################################################
class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        self.vertices["%s" %(vertex)] = []
    
    def addEdge(self,origin,destination,weight):
        if not (destination in self.vertices["%s" % (origin)]):
            self.vertices["%s" % (origin)].append({destination:weight})
###################################################################################################
array =open('TextGraph.txt','r').read().split('\n')

#word = int(word[word.index(':')+1:len(word):])

def arrayToGraph(array,G,initValue=0,currentVertex=None):
	if(initValue+5<=len(array)):
		if(' ' not in array[initValue]):

			#agregar vertice
			return arrayToGraph(array,G,initValue+1,array[initValue][:1:])

		else:

			values = []
			for i in range(1,6):
				values.append(array[initValue+i][array[initValue+i].index(':')+1:len(array[initValue+i]):])
			#calcular peso
			weight = getWeight(int(values[0]),int(values[1]),int(values[2]),int(values[3]),values[4])
			G.addEdge(currentVertex,array[initValue][1:2:].strip(),weight)
			#agregar arista en currentVertex
			return arrayToGraph(array,G,initValue+6,currentVertex)

G = Graph()
for i in range(len(array)):
	if(' ' not in array[i]):
		if(array[i] != ''):
			G.addVertex(array[i][:1:])

arrayToGraph(array,G)
print(G.vertices)