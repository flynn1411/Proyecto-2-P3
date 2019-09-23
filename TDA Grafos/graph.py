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

    def getAllPaths(self, currentVertex, destination, visited = [], path = [], fullPath = [], weight = 0):
       # get vertex, it is now visited and should be added to path
       vertex = self.vertices[currentVertex]
       visited.append(currentVertex)
       path.append(vertex.name)

       # save current path if we found end
       if (currentVertex == destination):
           fullPath.append({"weight": weight, "path": list(path)})

       for edge, value in vertex.edges.items():
           if edge not in visited:
               #self.vertices[edge].currCost = vertex.get_cost(edge) + vertex.currCost
               self.getAllPaths(edge, destination, visited, path, fullPath, weight + value)

       # continue finding paths by popping path and visited to get accurate paths
       path.pop()
       visited.pop()

       if not path:
           return fullPath

    def sortPaths(self, array):
        #Setting the range for comparison (first round: n, second round: n-1  and so on)
        for i in range(len(array)-1,0,-1):
            #Comparing within set range
            for j in range(i):
                #Comparing element with its right side neighbor
                if array[j]["weight"] > array[j+1]["weight"]:
                    #swapping
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

        return array


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")

g.addEdge("A", "B", 4)
g.addEdge("A", "C", 2.5)

g.addEdge("B", "C", 0.5)
g.addEdge("B", "A", 2)
g.addEdge("B", "D", 4)

g.addEdge("C", "D", 1)
g.addEdge("C", "A", 3)
g.addEdge("C", "B", 1)

g.addEdge("D", "C", 3)
g.addEdge("D", "B", 4)


for k,v in g.vertices.items():
    print("%s: %s" %(k, v.edges))

print("\n")
paths = g.getAllPaths("A", "D")
print("\n")
for path in paths:
    weight = path["weight"]
    actualPath = path["path"]

    print("El camino es %s con peso total de %s" %(actualPath, weight))

print("\nSorteados de menor mayor:")

sortedPaths = g.sortPaths(paths)

for path in sortedPaths:
    weight = path["weight"]
    actualPath = path["path"]

    print("El camino es %s con peso total de %s" %(actualPath, weight))