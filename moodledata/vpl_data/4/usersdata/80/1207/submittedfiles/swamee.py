# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('digite o valor de f:')
L=input('digite o valor de L:')
Q=input('digite o valor de Q:')
dH=input('digite o valor de dH:')
v=input('digite o valor de v:')

g=9.81
e=0.000002
D=(((8*f*L*(Q**2))/((3.14159**2)*g*dH))**0.2)
Rey=(4*Q)/(3.14159*D*v)
k=(0.25)/((math.log10((e)/(3.7*D))+((5.74)/(Rey**0.9)))**2)

print('o valor de D: %.4f' %D)
print('o valor de Rey: %.4f' %Rey)
print('o valor de k: %.4f' %k)


