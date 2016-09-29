# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input('digite o valor de f:')
l = input('digite o valor de l:')
q = input('digite o valor de q:')
h = input('digite o valor de h:')
v = input('digite o valor de v:')
g = 9.81
e = 0.000002
pi = 3,1415
D=(((8*f*l*(q**2))/((pi**2)*g*h)))**(0.2)
rey=(4*q)/(pi*D*v)
k=(0.25)/((math.log10((e/(3.7*D))+(5.74/(rey**(0.9)))))**2)
print('%.4f' %D)
print('%.4f' %rey)
print('%.4f'%k)