import math
from graph import *

class Loader:
    def __init__(self):
        self.G = Graph()

    def arrayToGraph(self, array, initValue=0, currentVertex=None):
        if(initValue+5<=len(array)):
            if(' ' not in array[initValue]):

                #agregar vertice
                return self.arrayToGraph(array, initValue+1, array[initValue][:1:])

            else:

                values = []
                for i in range(1,6):
                    values.append(array[initValue+i][array[initValue+i].index(':')+1:len(array[initValue+i]):])
                #calcular peso
                weight = self.getWeight(int(values[0]),int(values[1]),int(values[2]),int(values[3]),values[4])
                self.G.addEdge(currentVertex,array[initValue][1:2:].strip(),weight)
                #agregar arista en currentVertex
                return self.arrayToGraph(array, initValue+6,currentVertex)


    def getTrust(self, mediumType, distance):
        trustworthiness = 1
        trust = 0.00

        if(mediumType == "CAT5"):
            n = math.floor(distance/50)
            trust = 0.0002*n

        elif(mediumType == "CAT6"):
            n = math.floor(distance/50)
            trust = 0.0001*n

        elif(mediumType == "Fibra"):
            n = math.floor(distance/100)
            trust = 0.0005*n

        elif(mediumType == "WIFI"):
            n = math.floor(distance/6)
            trust = 0.006*n

        elif(mediumType == "Coaxial"):
            n = math.floor(distance/100)
            trust = 0.0004*n

        else:
            n = math.floor(distance/100)
            trust = 0.0001*n

        return (float(trustworthiness) - trustworthiness*trust)


    def getWeight(self, distance, bandwidth, users, traffic, medium):

        return round( ((bandwidth/self.getTrust(medium, distance) - bandwidth)+( (users+traffic)/bandwidth)) , 2)



array = open('TextGraph.txt','r').read().split('\n')

loader = Loader()
loader.arrayToGraph(array)

for k,v in loader.G.vertices.items():
    print("%s: %s" %(k, v.edges))