# -*- coding: utf-8 -*-
from __future__ import division
import math

#entrada

f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
deltaH=input('Digite o valor de deltaH:')
v=input('Digite o valor de v:')

#processamento

g=(9.81)
e=(0.000002)
D=(8*f*L*(Q**2))/((math.pi**2)*9.81*deltaH)**0.2
Rey=(4*Q)/(math.pi*D*v)
k=0.25/(math.log10(0.000002/(3.7*D))+(5.74/(Rey**0.9)))))**2

#saida

print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)