# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
f=input('digite um valor de f:')
L=input('digite um valor de L:')
Q=input('digite um valor de Q:')
deltaH=input('digite um valor de deltaH:')
V=input('digite um valor de v:')
#processamento
g=9,81
e=0,000002
D=(8*f*L*(Q**2)/((math.pi**2)*g*deltaH))**0.2
Rey=(4*Q)/(math.pi*D*V)
k=0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2

print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)