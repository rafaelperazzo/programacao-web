# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#entrada
f = input ('Digite um valor para f: ')
L = input ('Digite um valor para L: ')
Q = input ('Digite um valor para Q: ')
deltaH = input ('Digite um valor para deltaH: ')
v = input ('Digite um valor para v: ')

#processamento:
g= 9.81
E = 0.000002

D = (( 8*f*L*(Q**2))/((math.pi**2)*g*deltaH))**0.2
Rey = (4*Q)/(math.pi*D*v)
x = (E/(3.7*D)) + (5.74/(Rey**0.9))
k = 0.25 / (log10(x)**2

#saída
print (' %.3f' %D )
print (' %.3f' %Rey )
print (' %.4f' %k )