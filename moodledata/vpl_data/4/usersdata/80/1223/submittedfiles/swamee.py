# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('digite o valor de f:')
L=input('digite o valor de L:')
Q=input('digite o valor de Q:')
dH=input('digite o valor de dH:')
v=input('digite o valor de v:')

pi=3.14159265359
D=(((8*f*L*(Q**2))/((pi**2)*9.81*dH))**0.2)
Rey=(4*Q)/(pi*D*v)
k=(0.25)/((math.log10((0.000002)/(3.7*D))+((5.74)/(Rey**0.9)))**2)

print('o valor de D: %.4f' %D)
print('o valor de Rey: %.4f' %Rey)
print('o valor de k: %.4f' %k)


