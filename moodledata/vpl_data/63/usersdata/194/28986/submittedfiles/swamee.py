# -*- coding: utf-8 -*-
import math
f=float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
DeltaH=float(input('Digite DeltaH:'))
v=float(input('Digite v:'))
g=9.81
e=0.000002
D=((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
K=O.25/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2
print('Valor de D é: %.4f' %D)
print('Valor de Rey é: %.4f' %Rey)
print('Valor de K é: %.4f' %K)