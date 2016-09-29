# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
f=input('Digite o valor de f:')
L=input('Digite o valor de L:')
Q=input('Digite o valor de Q:')
DeltaH=input('Digite o valor de DeltaH')
V=input('Digite o valor de V:')

#PROCESSAMENTO
g=9.81
E=0.000002

D=((8*f*L*(Q**2))/((3.14159265359**2)*g*DeltaH))**0.2
Rey=(4*Q)/(3.14159265359*D*V)
K=(0.25)/(math.log10((E/(3.7*D))+(5.74/(Rey**0.9))))**2

#SAÍDA
print('D=%.4f'%(D))
print('Rey=%.4f'%(Rey))
print('k=%.4f'%(K))