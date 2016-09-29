# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f= input(' digite o valor de f:')
l= input(' digite o valor de l: ')
q=input(' digite o valor de q: ')
h= input(' digite o valor de delta h: ')
v= input( ' digite o valor de v: ')
g= 9.81
e= 0.000002
pi= math.pi
d= ((8*f*l)*(q**2)/((pi**2)*g*h))**0.2
rey= (4*q)/(pi*d*v)
k= 0.25/(math.log10((e/(3.7*d)) + (5.74/(rey**0.9)))**2
print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%k)