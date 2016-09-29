# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input('')
l = input('')
q = input('')
dH = input('')
v = input('')

d = ((8*f*k*q*q)/(math.pi*math.pi*9.81*dH)))**(1/5)
rey = (4*q)/(math.pi*d*v)

a = 0.000002/(3.7*d)
b = 5.74/(rey**0.9)

k = 0.25/(math.log10(a+b))**2

print('D=%.4f'% d)
print('Rey=%.4f'% rey)
print('k=%.4f'% k)