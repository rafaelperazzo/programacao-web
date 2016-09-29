# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input ('Digite o valor de f:')
l=input ('Digite o valor de l:')
q=input ('Digite o valor de q:')
dh=input ('Digite o valor de dh:')
v=input ('Digite o valor de v:')

g=9.81
e=0.000002

D = ((8*f*1*(q*q))/(((math.pi)**2)*g*dh))**0.2
Rey = (4*q)/((math.pi)*D*v)
k = (0.25)/((math.log10(((e)/(3.7*D)) + ((5.74)/((Rey)**0.9))))**2)
print ('D=5.4f' %D)
print ('Rey=%.4f' %Rey)
print ('k=%.4f' %k)