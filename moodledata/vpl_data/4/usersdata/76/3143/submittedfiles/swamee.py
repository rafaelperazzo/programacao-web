# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = 0.2
L = 50000
Q = 0.65
DeltaH = 2
v = 0.000001
g = 9.81
e = 0.000002

D1 = (8*f*L*(Q**2))
D2 = (math.pi**2)*g*DeltaH

D = (D1/D2)**0.2
Rey = ((4*Q)/((math.pi)*D*v))

k1 = e/(3.7*D)
k2 = 5.74/(Rey)**0.9

k = (0.25)/(math.log10((k1)+(k2)))**2

print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)
