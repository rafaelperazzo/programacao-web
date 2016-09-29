# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f = input('Digite o valor de f:')
l = input('Digite o valor de l:')
q = input('Digite o valor de q:')
deltah = input('Digite o valor de DeltaH:')
v = input('Digite o valor de v:')

x = (8*f*l*q**2)/(((math.pi)**2)*9.8*deltah)
d = math.pow(x,1/5)

Rey= ((4*q)/((math.pi)*d*v))

y = (0.000002/(3.7*d))+(5.74/(Rey**(9/10)))
k = (0.25)/((math.log10(y))**2)

print ('D é igual a %.4f'% d)
print ('Rey é igual a %.4f' % Rey)
print ('K é igual a %.4f' % k)
