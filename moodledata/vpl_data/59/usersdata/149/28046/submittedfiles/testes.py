# -*- coding: utf-8 -*-
import math
f=float(input('digite o valor de f:'))
L=float(input('digite o valor de L:'))
Q=float(input('digite o valor de Q:'))
DeltaH=float(input('digite o valor de deltaH:'))
g=9.81
e=0.000002
D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH)**0.2)
print('%.4f'%D) 