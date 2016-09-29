# -*- coding: utf-8 -*-
from __future__ import division
import math

F = input ('Digite o valor de f: ')
l = input ('Digite o valor de L: ')
q = input ('Digite o valor de Q: ')
a = input ('Digite o valor de delta H: ')
v = input ('Digite o valor de v: '

D = ((8*F*l*(q)**2)/(9.81*a*math.pi**2))**(1.0/5)

Rey = 4*q/math.pi*D*v

K = 0.25/(math.log10(0.000002/3.7*D+5.74/(Rey)**0.9)**2

print ('D=%.4f'%D)
print ('Rey=%.4f'%Rey)
print ('k=%.4f'%k)
