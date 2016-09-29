# -*- coding: utf-8 -*-
from __future__ import division
import math

f= input('Digite o valor de f:')
L= input('Digite o valor de L:')
Q= input('Digite o valor de Q:')
DeltaH= input('Digite o valor de Delta H')
v= input('Digite o valor de v')
g= 9.81
e= 0.000002
D=((8*f*L*Q*Q)/((math.pi)**2(g*DeltaH))**(1/5)
Rey=(4*Q)/(math.pi*D*v)
K=(0.25)/(math.log10((e/3.7*D)+(5.74)/(Rey)**0.9))**2
print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('K=%.4f'%K)