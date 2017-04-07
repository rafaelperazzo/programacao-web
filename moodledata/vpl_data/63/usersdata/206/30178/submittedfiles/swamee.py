# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f= float(input('Digite f:'))
L=float(input('Digite L:'))
Q=float(input('Digite Q:'))
deltaH=float(input('Digite deltaH:'))
v=float(input('Digite v:'))

g=9.87
e=0.000002 

D=((8*f*L*(Q**2))/(math.pi**2)*g*deltaH)**0.2

Rey=(4*Q)/(math.pi*D*v)

k=(0.25)/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9))**2

print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%k)