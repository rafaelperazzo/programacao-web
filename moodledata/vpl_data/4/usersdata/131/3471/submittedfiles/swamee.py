# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f = input('digite o valor de f: ')

l = input('digite o valor de l: ')

q = input('digite o valor de q: ')

dh = input('digite o valor de dh: ')

v = input('digite o valor de v: ')

e=0.000002

g=9.81

D = ((8*f*l*(q**2.0))/((math.pi**2.0)*g*dh))**(1/5.0)

rey = (4*q)/((math.pi)*D*v)

k = 0.25/((math.log10((e/(3.7*D))+(5.74/rey**(0.9))))**2)

print('valor de D = %.4f ' % D)
print('valor de rey = %.4f ' % rey)
print('valor de k = %.4f ' % k)