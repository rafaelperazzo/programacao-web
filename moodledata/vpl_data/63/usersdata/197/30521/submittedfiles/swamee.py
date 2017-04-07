# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
deltah=float(input('Digite o valor de deltah:'))
v=float(input('Digite o valor de v:'))
g=9.81
e=0.000002
math.pi
D=((8*f*l*q*q)/((math.pi**2)*g*deltah))**(1/5)
print('D=%.4f'%D)
Rey=(4*q)/((math.pi)*D*v)
print('Rey=%.4f'%Rey)
k=((0.25)/(math.log10((e)/(3.7*D) + (5.74)/(Rey**0.9))(**2)))
print('k=%.4f'%k)