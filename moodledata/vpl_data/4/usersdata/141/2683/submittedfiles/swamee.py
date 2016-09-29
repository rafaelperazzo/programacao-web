# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('digite o valor de f:')
L=input('digite o valor de L:')
Q=input('digite o valor de Q:')
DeltaH=input('digite o valor de DeltaH:')
v=input('digite o valor de v:')
g=9.81
e=0.000002
D=((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**0.2
Rey=((4.Q)/(math.pi*D*v))
k=(0.25)/((math.log10((e/3.7*D)+((5.74)/(Rey**0.9))))**2
print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)

