# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
g = 9.8
e = 0.000002
f = float(input('digite o valor de f='))
l = float(input('digite o valor de l='))
q = float(input('digite o valor de q='))
dh = float(input('digite o valor de dh='))
v = float(input('digite o valor de v='))
D = (8*f*l*(q**2)/(math.pi**2)*g*dh)**1/5
print('%.4f' % D)
