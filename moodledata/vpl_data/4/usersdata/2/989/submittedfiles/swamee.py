# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f = input('Digite f: ')
L = input('Digite L: ')
Q = input('Digite Q: ')
deltaH = input('Digite Delta H: ')
v = input('Digite v:')

g = 9.81
e = 0.000002

D = ((8*f*L*Q*Q)/(math.pi*math.pi*g*deltaH))**(0.2)
Rey = (4*Q)/(math.pi*D*v)

formula1 = e/(3.7*D)
formula2 = 5.74/(Rey**0.9)
formula3 = math.log10(formula1+formula2)

f = 0.25/(formula3**2)

print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % f)

