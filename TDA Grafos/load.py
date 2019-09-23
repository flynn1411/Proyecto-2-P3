import math
from graph import *
import networkx as nx
import matplotlib.pyplot as plt

class Loader:
    def __init__(self):
        self.G = Graph()

    def load(self, array):
        #Se agregan todos los vertices al grafo
        for i in range(len(array)):
            if(' ' not in array[i]):
                if(array[i] != ''):
                    self.G.addVertex(array[i][:array[i].index(':'):])

        self.arrayToGraph(array)

    def arrayToGraph(self, array, initValue=0,currentVertex=None):
        #Condicion de salida para recursividad
        #Se pregunta si el valor acual es igual o menor a la cantidad total de elementos del array si se le suma 5(esta
        #cantidad , por que 5 es la cantidad de elementos que tiene una arista)
        if(initValue+5<=len(array)):
            #Se comprueba si el primer elemento tiene espacios en su nombre
            if(' ' not in array[initValue]):

                #Se cambia el currenVertex por el initvalue del array y se suma 1 a initValue para pasar a sus aristas
                return self.arrayToGraph(array, initValue+1,array[initValue][:len(array[initValue])-1:])

            else:
                #areglo que guarda los valores(usuarios,distancia,ancho de banda,medio) para calcular el peso
                values = []
                for i in range(1,6):
                    #Se itera el arreglo con initValues sumandole i(1,2,3,4,5) para recorrer los elementos de su arista
                    #se utiliza [::] que funcina asi [Valor de inicio:Valor tope:Paso]
                    #Se inicia desde el indice donde aparece ':' +1 y termina en el tamaño de la cadena 
                    values.append(array[initValue+i][array[initValue+i].index(':')+1:len(array[initValue+i]):])
                #Se calcula el peso
                weight = self.getWeight(int(values[0]),int(values[1]),int(values[2]),int(values[3]),values[4])
                self.G.addEdge(currentVertex,array[initValue].strip()[:len(array[initValue])-2:],weight)
                #Se pasa a la siguiente arista/vertice sumandole 6 a initValue y pasando nuevamente el nombre del vertice actual
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

        return round( ((bandwidth/self.getTrust(medium, distance) - bandwidth)+( (users+traffic)/bandwidth))*10 , 2)





