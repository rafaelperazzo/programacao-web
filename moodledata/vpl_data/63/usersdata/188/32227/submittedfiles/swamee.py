# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite aqui o valor de f:'))
L=float(input('Digite aqui o valor de L:'))
Q=float(input('Digite aqui o valor de Q:'))
DeltaH=float(input('Digite aqui o valor de Delta H:'))
V=float(input('Digite aqui o valor de V:'))
g=9.81
E=0.000002
math.pi3.14159
D=((8*f*L*(Q**2)))/((math.pi**2*g*DeltaH)**0.2)
Rey=(4*Q)/(math.pi*D*V)
k=0.25/((math.log10((E/3.7*D))+(5.74)/(Rey**0.9)))**2
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%k)
