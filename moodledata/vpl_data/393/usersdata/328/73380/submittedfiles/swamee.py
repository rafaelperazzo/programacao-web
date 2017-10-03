# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

f=float(input('Digite o valor de f:'))
L=float(input('Digite o valor de L:'))
Q=float(input('Digite o valor de Q:'))

deltaH=float(input('Digite o valor de deltaH:'))
v=float(input('Digite o valor de v:'))
g=9.81
e=0.000002
D=(((8*f*L*Q**2)/((math.pi)**2*g*deltaH))**0.2)
print('%.4f'%D)

#Calcular o Rey

Rey=((4*Q)/(math.pi*D*v))
print('%.4f'%Rey)

#Calcular o k

k = ((0.25)/((math.log10(((e)/(3.7*D)) + ((5.74)/(Rey**0.9))))**2)
print('%.4f'%k)