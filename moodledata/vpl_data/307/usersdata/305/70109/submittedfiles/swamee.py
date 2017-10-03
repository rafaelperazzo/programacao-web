# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('digite o valor de f'))
L = float(input('digite o valor de L'))
Q = float(input('digite o valor de Q'))
DeltaH = float(input('digite o valor de DeltaH'))
v = float(input('digite o valor de v'))
g = 9.81
e = 0.000002
D = ((8*f*L*Q**2)/(math.pi*g*DeltaH**2))**0.2
