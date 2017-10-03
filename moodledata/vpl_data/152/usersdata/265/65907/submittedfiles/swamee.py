# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('digite o valor de f: '))
L = float(input('digite o valor de L: '))
Q = float(input('digite o valor de Q: '))
DeltaH = float(input('digite o valor de DeltaH: '))
Omega = float(input('digite o valor de Omega: '))
g = 9.81
E = 0.000002
PI = math.pi
D = ((8*f*L*(Q**2))/((PI**2)*g*DeltaH))**(1/5)
