# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input('Digite o valor de f:')
L = input('Digite o valor de L:')
Q = input('Digite o valor de Q')
H = input('Digite o valor de H')
V = input('Digite o valor de v')

g = 9.81
e = 0.000002

D = (8*f*L*(Q)**2)/(math.pi**2*g*H)

print('D=%.4f'%D)
