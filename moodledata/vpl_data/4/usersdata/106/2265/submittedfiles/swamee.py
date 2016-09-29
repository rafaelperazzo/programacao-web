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
D = (( 8*f*L*(Q**2))/((math.pi**2)*9.81*deltaH))**0.2
Rey = (4*Q)/(math.pi*D*v)
x = (0.000002/(3.7*D)) + (5.74/(Rey**0.9))
k = 0.25 / ((math.log10(x))**2)
#saída
print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k )