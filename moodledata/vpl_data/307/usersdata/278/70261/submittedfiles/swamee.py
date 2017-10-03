# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Digite f: '))
L = float(input('Digite L: '))
Q = float(input('Digite Q: '))
DeltaH = float(input('Digite DeltaH: '))
v = float(input('Digite v: '))
g = 9.81
e = 0.000001
pi = math.pi
D = ((8*f*L*Q*Q)/(pi*pi*g*DeltaH))**0.2
print('%.4f' %(D))
