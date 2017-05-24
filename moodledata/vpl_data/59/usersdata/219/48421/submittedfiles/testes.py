# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
deltah=float(input('Digite o valor de deltah:'))
v=float(input('Digite o valor de v:'))
g=9.81
e=0.000002
d=((8*f*l*(q**2))/(math.pi**2)*g*deltah)**0.2
rey=(4*q)/(math.pi*d*v)
k=(0.25)/((math.log10(((e)/(3.7*d))+((5.74)/(rey**0.9))))**0.2
print('d=%.4f'%d)
print('rey=%.4f'%rey)
print('k=%.4f'%k)
