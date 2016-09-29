# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = input ('digite o valor de f: ')
L = input (' digite o valor de L: ')
Q = input (' digite o valor de Q: ')
dH = input (' digite o valor de DeltaH: ')
v = input (' digite o valor de v: ')

g = 9.81
E = 0.000002

D = (((8*f*L*Q)**0.5)/((math.pi)**0.5)*g*dH)**0.2

Rey = 4*Q/math.pi*D*v

k = 0.25/(math.log10((E/3.7*D)+(5.74/Rey**0.9)))**2

print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)