# -*- coding: utf-8 -*-
from __future__ import division
import math

f= input('Digite o valor de f: ')
l= input('Digite o valor de l: ')
q= input('Digite o valor de q: ')
dh= input('Digite o valor de dh: ')
v= input('Digite o valor de v: ')

g= 9.81
e= 0.000002

d= (((8*f*L*(q**2))/((math.pi**2)*g*dh))**0.2)
rey= (4*q)/(math.pi*d*v)
k= 0.25/((math.log((e/(3.7*d))+(5.74/(rey**0.9))))**2)

print('d=%.4f'%d)
print('rey=%.4f'%rey)
print('k=%.4f'%k)