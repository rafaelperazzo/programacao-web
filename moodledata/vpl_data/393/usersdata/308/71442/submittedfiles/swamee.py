# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.81
e = 0.000002

f = float(input('Informe o valor de f: '))
l = float(input('Informe o valor de L: '))
q = float(input('Informe o valor de Q: '))
h = float(input('Informe o valor de dH: '))
v = float(input('Informe o valor de v: '))

d = ( (8*f*l*q*2)/(math.pi*g*h) )**(1/5)
print ('%.4f' % d)
