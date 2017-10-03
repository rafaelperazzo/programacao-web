# -*- coding: utf-8 -*-
import math
#constantes
g = 9.81
e = 0.000002

#recebendo variáveis
f = float(input('Informe o valor de f: '))
l = float(input('Informe o valor de L: '))
q = float(input('Informe o valor de Q: '))
h = float(input('Informe o valor de dH: '))
v = float(input('Informe o valor de v: '))

#calculando d
d = ( (8*f*l*q*q) / (math.pi*math.pi*g*h) )**(0.2)
print ('%.4f' % d)

#calculando rey
rey = (4*q)/(math.pi*d*v)
print ('%.4f' % rey)