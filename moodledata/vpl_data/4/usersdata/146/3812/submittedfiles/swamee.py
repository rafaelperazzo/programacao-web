# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input ('Digite o valor de f: ')
l = input ('Digite o valor de L: ')
q = input ('Digite o valor de Q: ')
dh = input ('Digite o valor de delta H: ')
v = input ('Digite o valor de v: ')
e = 0.000002

D = ((8*f*l*(q**2))/(math.pi**2)*9.81*dh)**0.2

Rey = 4*q/(math.pi*d*v)

k = 0.25/(math.log10(e/(3.7*d)+5.74/(Rey**0.9))**2)


print ('D = %.4f' %D) 
print ('Rey = %.4f' %Rey)
print ('K = %.4f' %k)
