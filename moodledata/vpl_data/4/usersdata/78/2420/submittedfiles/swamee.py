# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('digite o valor de f')
l=input('digite o valor de l')
q=input('digite o valor de q')
dh=input('digite o valor de dh')
v=input('digite o valor de v')

D=((8*f*l*(q**2))/(((math.pi)**2)*9.81*dh))**0.2
rey=(4*q)/((math.pi)*D*v)
k=0.25/(math.log10((0.000002/(3.7*D))+(5.74/(rey**0.9)))

print('resultado:%.4f' %D)
print('resultado:%.4f' %rey)
print('resultado:%.4f' %k
