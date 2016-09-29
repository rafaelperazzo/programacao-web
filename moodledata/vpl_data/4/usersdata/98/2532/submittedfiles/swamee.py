# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('Digite o valor de f: ')
l=input('Digite o valor de l: ')
q=input('Digite o valor de q: ')
h=input('Digite o valor de h: ')
o=input('Digite o valor de o: ')

g=9.81
e=0.000002

d=((8*f*l*(q**2))/((math.pi**2)*g*h))**(1/5)
rey=(4*q)/(math.pi*d*o)

k=(0.25)/((math.log10((e)/(3.7*d)+(5.74)/(rey**0.9)))**2)

print('%.4f' %d)
print('%.4f' %rey)
print('%.4f' %k)
