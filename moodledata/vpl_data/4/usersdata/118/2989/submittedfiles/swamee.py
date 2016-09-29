# -*- coding: utf-8 -*-
from __future__ import division
import math

#1
f = input('digite o valor de f =')
L = input('digite o valor de L =')
Q = input('digite o valor de Q =')
dH = input('digite o valor de Delta H =')
v = input('digite o valor de v =')

#2
g = 9.81
e = 0.000002

D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**(0.2)

Rey = (4*Q)/(math.pi*D*v)

k = (0.25/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2))

#3
print('D=%.4f' %D)

print('Rey=%.4f' %Rey)

print('k=%.4f' %k)