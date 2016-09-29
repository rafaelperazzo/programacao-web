# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = input ('Digite valor de f:')
L = input ('Digite valor de L:')
Q = input ('Digite valor de Q:')
DeltaH = input ('Digite valor de DeltaH:')
O = input ('Digite valor de O:')
g = 9.81
e = 0.000002

D = ((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**0.2
Rey = (4*Q)/(math.pi*D*O)
k = 0.25/(math.log10((e/3.7*D))+(5.74/(Rey**0.9)))**2

print ('D=%.4f'%D)
print ('Rey=%.4f'%Rey)
print ('k=%.4f'%k)