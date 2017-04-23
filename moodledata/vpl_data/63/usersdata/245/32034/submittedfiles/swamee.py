# -*- coding: utf-8 -*-
import math
# COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
dh=float(input('Digite o valor de Delta h:'))
v=float(input('Digite o valor de v:'))
e=0.000002
pi=math.pi
g=9.81
d=((8*f*l*q*q)**0.2)/((pi*pi*g*dh)**0.2)
rey=4*q/(pi*d*v)
k=0.25/(math.log10(e/(3.7*d)+5.74/(rey**0.9)))**2
print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%k)