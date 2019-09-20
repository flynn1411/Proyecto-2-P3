from vertex import *

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertexValue):
        newVertex = Vertex(vertexValue)
        self.vertices["%s" %(newVertex.name)] = newVertex

    def addEdge(self, origin, destination, weight):
        originVertex = self.vertices["%s" %origin]
        destinationVertex = self.vertices[destination]

        if not (destinationVertex.name in self.vertices["%s"%originVertex.name].edges):
            originVertex.setEdgeWith(destinationVertex.name, weight)

    def findPaths(self, vertex, destination, path = [], visited = [], weight = 0, route = 0):
        #Agrego el vertice actual a la ruta y lo marco como visitado(para evitar ciclos)
        paths = {}
        visited.append(vertex)
        path.append(vertex)

        #Si el vertice actual es mi destino, imprimo la ruta seguida
        if (vertex == destination):
            route
            paths["Ruta%s" %route] = {"path": path, "weight": weight}
            print("La ruta: %s con el peso %s"%(path, weight))

        #Si no es el destino, se iteran las aristas del vertice actual
        else:
            for edge, value in self.vertices["%s" %vertex].edges.items():
                #Si la arista actual no se encuentra en los visitados, se llama recursivamente la función 
                #para seguir avanzando
                if(not edge in visited):
                    self.findPaths(edge, destination, path, visited, weight+value, route)

        #Luego de encontrar el destino, se retrocede un paso para poder buscar mas posibles caminos
        path.pop()
        visited.pop()
        print(paths)


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")

g.addEdge("A", "B", 2)
g.addEdge("A", "C", 3)

g.addEdge("B", "C", 1)
g.addEdge("B", "A", 2)
g.addEdge("B", "D", 4)

g.addEdge("C", "D", 3)
g.addEdge("C", "A", 3)
g.addEdge("C", "B", 1)

g.addEdge("D", "C", 3)
g.addEdge("D", "B", 4)


for k,v in g.vertices.items():
    print("%s: %s" %(k, v.edges))

print("\n")
g.findPaths("A", "D")
"""paths = g.findPaths("A", "D")
print("\n")

for k,v in paths.items():
    print("%s: %s" %(k, v))"""