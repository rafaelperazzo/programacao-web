# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
dh=float(input('Digite o valor de dh:'))
v=float(input('Digite o valor de v :'))
e=0.000002
g=9.81
D=(((8*f*l*(q**2)))/((math.pi**2)*g*dh))**0.2
Rey=((4*q)/(math.pi*D*v))
k=(0.25)/(math.log(((e)/(3.7*D))+((5.74)/(Rey**0.9))))**2
print('D= %.4f'%D)
print('Rey= %.4f'%Rey)
print('k= %.4f'%k)

