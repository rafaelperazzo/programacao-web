# -*- coding: utf-8 -*-
import math
f=float(input('Digite o valor de f: '))
l=float(input('Digite o valor de l: '))
q=float(input('Digite o valor de q: '))
deltah=float(input('Digite o valor de deltaH: '))
v=float(input('Digite o valor de v: '))
g=float(9.81)
e=float(0.000002)

D=((8*f*l*(q**2))/((math.pi**2)*g*deltah))**0.2
Rey=(4*q)/(math.pi*d*v)
k=0.25/(math.log10((e/3.7*d))+(5.74)/(Rey**0.9)))**2

print('d=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)
