# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltah=float(input('digite deltah:'))
v=float(input('digite v:'))
g=9.81
e=0.000002
pi=math.pi
D=((8*f*l*(q**2))/((math.pi**2)*g*deltah))**(1/5)
Rey=(4*q)/(math.pi*D*v)
K=0.25/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2)
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%K)