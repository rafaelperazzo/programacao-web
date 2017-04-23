# -*- coding: utf-8 -*-
import math

f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
dh=float(input('Digite o valor de Delta h:'))
v=float(input('Digite o valor de v:'))
e=0.000002
pi=math.pi
d=(8*f*l*(q**2)**0.2/(pi*pi)*9.81*dh)**0.2
Rey=(4*q)/pi*d*v
k=0.25/(math.log10((e/(3.7*d))+(5.74)/(Rey**0.9))*2
print('%.4f'%d)
print('%.4f'%Rey)
print('%.4f'%k)