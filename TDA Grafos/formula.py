#Formula para el peso
import math
"""
FORMULA = (confiabilidad * ancho) - (usuarios + trafico)
hola = {"A": "holaaa"}

*distancia,
ancho de banda,
cantidad de usuarios,
cantidad de trafico,
*tipo de medio(relacion con la distancia)

Confiabilidad(double trust, double distance, trustworthiness = 1):

-CAT5: disminuye 0.02% de confiabilidad por cada 50 metros:
    if (distance >= 50):
        n = distance/50
    trust = 0.0002*n

    trustworthiness = trustworthiness - trust

-CAT6: disminuye 0.01% de confiabilidad por cada 50 metros:
    if (distance >= 50):
        n = distance/50
    trust = 0.0001*n

    trustworthiness = trustworthiness - trust

-Fibra-Óptica: disminuye 0.05% de confiabilidad por cada 100 metros:
    if (distance >= 100):
        n = distance/100
    trust = 0.0005*n

    trustworthiness = trustworthiness - trust 

-WIFI: disminuye 0.6% de confiabilidad por cada 6 metros:
    if (distance >= 6):
        n = distance/6
    trust = 0.006*n

    trustworthiness = trustworthiness - trust

-Coaxial: disminuye 0.04% de confiabilidad por cada 100 metros:
    if (distance >= 100):
        n = distance/100
    trust = 0.0004*n

    trustworthiness = trustworthiness - trust

-Par-Trenzado: disminuye 0.01% de confiabilidad por cada 100 metros:
    if (distance >= 100):
        n = distance/100
    trust = 0.0001*n

    trustworthiness = trustworthiness - trust 
"""

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

    return (float(trustworthiness) - trust)

formula1 = (getTrust("WIFI", 6)*15) -(3 + 4)
print(formula1)

formula2 = (getTrust("WIFI", 4)*10) -(1 + 4)
print(formula2)