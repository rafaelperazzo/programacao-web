# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('Digite o valor de f:')
l=input('Digite o valor de l:')
q=input('Digite o valor de q:')
deltah=input('Digite o valor de deltah:')
v=input('Digite o valor de v:')
D = ((8*f*l*(q*q))/(((math.pi)**2)*9.81*deltah))**0.2
Rey = (4*q)/((math.pi)*D*v)
k = (0.25)/((math.log10(((0.000002)/(3.7*D)) + ((5.74)/((Rey)**0.9))))**2)
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)
