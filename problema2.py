##Problema 2
from math import *

print("calcular la nota final del curso")
parcialuno= float(input("ingrese valor del parcial uno : "))
parcialdos= float(input("ingrese valor del parcial dos : " ))
taller= float(input("ingrese valor del taller : "))
proyecto= float(input("ingrese valor del proyecto : " ))
notaFinal = (parcialuno*0.25 + parcialdos*0.25 + taller*0.20 + proyecto*0.30)

if parcialuno <= 5 and parcialdos <= 5 and taller <=5 and proyecto <= 5:
    print( "la nota final es: " , notaFinal)
else:
    print(" No es correcto ")
