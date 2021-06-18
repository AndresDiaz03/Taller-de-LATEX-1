##Problema 4

from math import *

def dolares(pesos):
    dolares= float(pesos / 3517)//1
    ganancia=float(pesos*0.2)//1
    Gcasa= dolares-ganancia
    print(dolares)
    return(Gcasa)

def yenes(pesos):
    yenes= float(pesos/34.52)//1
    ganancia=float(pesos*0.2)//1
    Gcasa= yenes-ganancia
    print(yenes)
    return(Gcasa)

def euros(pesos):
    euros= float(pesos/ 4.313)//1
    ganancia=float(pesos*0.2)//1
    Gcasa= euros-ganancia
    print(euros)
    return(Gcasa)

dolares(8000)
yenes(8000)
euros(8000)
