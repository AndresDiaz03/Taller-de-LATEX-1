# Taller-de-LATEX-1
\author{Andres Felipe Diaz, Pontifica Universidad Javeriana}

\date{18/06/2021}

\maketitle

\section*{Problema 1}

Elaborar un algoritmo para calcular el área de un triángulo cuya altura es de 30 cm y la base de 50 cm. Realizar una versión genérica de este algoritmo para calcular el área de un triángulo dada una altura y una base cualquiera, ¿Qué cambio se debe hacer?


\begin{lstlisting}[label={list:first},caption=Código 1]
from math import *

altura= 50
base= 30
area= (base*altura)/2
print("la area del triangulo es: ", area)
