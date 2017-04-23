# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite aqui o valor de f:'))
L=float(input('Digite aqui o valor de L:'))
Q=float(input('Digite aqui o valor de Q:'))
DH=float(input('Digite aqui o valor de Delta H:'))
V=float(input('Digite aqui o valor de V:'))
g=9.81
E=0.000002
math.pi=3.14159
D=((8*f*L*(Q**2)))/((math.pi**2*g*DH)**0.2)
Rey=(4*Q)/(math.pi*D*V)
k=(0.25)/(math.log10((E)/3.7*D)+(5.74)/((Rey**0.9)))**2
print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)
