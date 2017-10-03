# -*- coding: utf-8 -*-
import math
#ENTRADA
f = float(input('Valor de f: '))
L = float(input('Valor de L: '))
Q = float(input('Valor de Q: '))
dtlH = float(input('Valor de DeltaH: '))
v = float(input('Valor de v: '))
#PROCESSAMENTO
g = 9.81
e = 0.000002
pi = math.pi
D = (((8)*(f)*(L)*(Q**2))/(pi**2)*(g)*(dtlH))**(1/5)