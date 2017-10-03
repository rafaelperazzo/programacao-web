# -*- coding: utf-8 -*-
import math

g = 9.81
e = 0.000002

f = float(input('Digite o valor de f: '))
L = float(input('Digite o valor de L: '))
Q = float(input('Digite o valor de Q: '))
DeltaH = float(input('Digite o valor de DeltaH: '))
v = float(input('Digite o valor de v: '))


D = ( (8*f*L*(Q**2))/((math.pi**2)*g*DeltaH) ) ** 0.2

print('D = {:.4f} '.format(D))