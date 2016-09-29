# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('Digite o valor f:')
L=input('Digite o valor L:')
Q=input('Digite o valor Q:')
DeltaH=input('Digite o valor DeltaH:')
v=input('Digite o valor v:')

g= 9.81
e= 0.000002

D=((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
k=(0.25)/(math.log10((e/(3.7*D))+(5.74/Rey**0.9))**2)

print('%.4f'% D)
print('%.4f'% Rey)
print('%.4f'% k)

