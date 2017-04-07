# -*- coding: utf-8 -*-
import math
f=float(input('digite o valor de f:'))
L=float(input('digite o valor de L:'))
Q=float(input('digite o valor de Q:'))
DeltaH=float(input('digite o valor de DeltaH:'))
v=float(input('digite o valor de v:'))
g=9.81
e=0.000002
D=((8*f*L*Q*Q)/(math.pi*math.pi*g*DeltaH))**0.2
Rey=(4*Q)/(math.pi*D*v)
k=0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2
print('o valor de D é:%.4f'%D)
print('o valor de Rey é:%.4f'%Rey)
print('o valor de k é:%.4f'%k)