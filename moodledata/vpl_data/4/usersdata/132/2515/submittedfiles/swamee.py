# -*- coding: utf-8 -*-
from __future__ import division
import math
f=input(' digite o valor de f: ')
L=input(' digite o valor de l: ')
Q=input(' digite o valor de q: ')
h=input(' digite o valor de  delta h: ')
v=input(' difite o valor de v: ')
g=9.81
e=0.000002
D=(((8*f*L*(q**2)))/((math.pi**2)*g*h))**(0.2)
Rey=((4*Q)/(math.pi*D*v))
k= 0.25/(math.log10((e/(3.7*d)+(5.74/(Rey**0.9)))))**2
print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%k)