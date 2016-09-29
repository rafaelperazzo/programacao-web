# -*- coding: utf-8 -*-
from __future__ import division
import math

f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))
DeltaH=float(input('Digite o valor de DeltaH:'))
v=float(input('Digite o valor de v:'))
g=9.81
E=0.000002

D=((((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH)))**(1/5))
Rey=(4*Q)/(math.pi*D*v)
k=(0,25)/((math.log10(E/3.7*D+(5.74/(Rey**0.9))))**2)

print('D:%.4f'%D)
print('Rey:%.4f'%Rey)
print('k:%.4f'%k)