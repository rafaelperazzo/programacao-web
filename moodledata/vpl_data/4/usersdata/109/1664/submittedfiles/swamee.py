# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada
f = input('Digite o valor de f:')
L = input('Digite o valor de L:')
Q = input('Digite o valor de Q:')
H = input('Digite o valor de H:')
V = input('Digite o valor de v:')

#Processamento
g = 9.81
e = 0.000002

D = ((8*f*L*(Q**2))/(math.pi**2*g*H))**0.2
Rey = (4*Q)/(math.pi*D*V)
K = (0.25)/(math.log10(e/(3.7*D)+5.74/(Rey**0.9))**2)

#Saída
print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('K=%.4f'%K)
