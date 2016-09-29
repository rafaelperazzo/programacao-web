# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA:
f = input('Digite o valor de f:')
L = input ('DIgite o valor de L:')
Q = input ('Digite o valor de Q:')
DeltaH = input ('Digite o valor de DeltaH:')
O = input ('Digite o valor de O:')
g = 9.81
e = 0.000002

#PROCESSAMENTO:
D = ((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**0.2
Rey = (4*Q)/(math.pi*D*O)
k = 0.25/(math.log10((e/3.7*D)+(5.74/Rey**0.9)))**2

#SAIDA:
print ('D=%.4f'%D)
print ('Rey=%.4f'%Rey)
print ('k=%.4f'%k)

