# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = input('Digite o valor de f:')
L = input('Digite o valor de L:')
Q = input('Digite o valor de Q:')
DeltaH = input('Digite o valor de DeltaH:')
v = input('Digite o valor de v:')
g = 9.81
e = 0.000002

D1 = (8*f*L*(Q**2))
D2 = (math.pi**2)*g*DeltaH

D = (D1/D2)**0.2
Rey = ((4*Q)/((math.pi)*D*v))
k = (0.25)/(math.log10((e/3.7*D)+(5.47/Rey**0.9)))**2

print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)
