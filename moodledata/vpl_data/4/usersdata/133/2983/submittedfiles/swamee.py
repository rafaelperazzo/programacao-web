# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('Digite o valor de f:')
l=inpnut('Digite o valor de l:')
q=input('Digite o valor de q:')
deltah=input('Digite o valor de deltah:')
v=input('Digite o valor de v:')

g=9.81
e=0.000002

D = ((8*f*l*(q*q))/(((math.pi)**2)*g*deltah))**0.2
Rey = (4*q)/((math.pi)*D*v))
k = (0.25)/((math.log10(((e)/(3.7*D)) + ((5.74)/((Rey)**0.9))))**2)
print('D=%.4f' %D)
print('Rey=%.4f' %Rey)
print('k=%.4f' %k)
