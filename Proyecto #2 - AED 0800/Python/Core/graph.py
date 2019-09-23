from Core.vertex import *

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertexValue):
        newVertex = Vertex(vertexValue)
        self.vertices["%s" %(newVertex.name)] = newVertex

    def addEdge(self, origin, destination, weight):
        originVertex = self.vertices["%s" %origin]
        destinationVertex = self.vertices[destination]

        if not (destinationVertex.name in originVertex.edges):
            originVertex.setEdgeWith(destinationVertex.name, weight)

    def getAllPaths(self, currentVertex, destination, visited = [], path = [], fullPath = [], weight = 0):
       #Se obtiene el objeto Vertex usando su nombre como llave, Se agrega su nombre en los visitados y el camino actual
       vertex = self.vertices[currentVertex]
       visited.append(vertex.name)
       path.append(vertex.name)

       #Si el vertice actual es el vertice destino, agregar el camino actual al arreglo de caminos
       if (currentVertex == destination):
           fullPath.append({"weight": round(weight, 3), "path": list(path)})

        #iterar el diccionario de aristas del vertice actual
       for edge, value in vertex.edges.items():
           if edge not in visited:
               #si el certice arista actual no se encuentra en los visitados, continuar en la busqueda a profundidad
               #sumandole el peso en el camino
               self.getAllPaths(edge, destination, visited, path, fullPath, weight + value)

       #Se remueve el vertice actual luego de iterar sus aristas para ir hacia atras y revisar si existen otros
       #posibles caminos
       path.pop()
       visited.pop()

       if not path:
           #Si el arreglo del camino actual está vacío, significa que ya se ha buscado en todos los vertices
           #Se retorna el arreglo de caminos ordenados de menor a mayor peso usando ordenamiento de burbuja
           return self.sortPaths(fullPath)

    def sortPaths(self, array):
        for i in range(len(array)-1,0,-1):
            for j in range(i):
                #Comparación de caminos usando su peso total
                if array[j]["weight"] > array[j+1]["weight"]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

        return array