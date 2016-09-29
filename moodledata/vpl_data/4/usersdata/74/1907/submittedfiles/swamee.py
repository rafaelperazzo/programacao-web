# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input('Digite o valor de f:')
l = input('Digite o valor de L:')
q = input('Digite o valor de Q:')
dH = input('Digite o valor de deltaH:')
o = input('Digite o valor de teta:')

d = ((8*f*k*q*q)/(math.pi*math.pi*9.81*dH))**(1/5)
rey = (4*q)/(math.pi*d*o)

a = 0.000002/(3,7*d)
b = 5.74/(rey**0,9)

k = 0.25/(math.log10(a+b))**2

print('%.4f %.4f %.4f %.4f'% (d,rey,k))