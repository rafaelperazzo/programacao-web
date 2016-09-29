# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

f = input ('Digite o valor de f: ')
L = input ('Digite o valor de L: ')
Q = input ('Digite o valor de Q: ')
dh = input ('Digite o valor de delta H: ')
v = input ('Digite o valor de v: ')

#Exe

D = ((8*f*L*Q**2)/(dh*9.81*math.pi**2))**(1.0/5)

Rey = 4*Q/(math.pi*D*v)

K = (0.25/(math.log10(0.000002/3.7*D+5.74/(Rey)**0.9)**2)

#Saida

print = ('d = %.4f' %D )
print = ('rey = %.4f' %Rey )
print = ('k = %.4f' %K )
