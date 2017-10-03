# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f: '))
l=float(input('digite l: '))
q=float(input('digite q: '))
h=float(input('digite h: '))
v=float(input('digite v: '))
g=(9.81)
e=(0.000002)
d=(((8*f*l*q**2)/(math.pi**2*g*h))**0.2)
rey=((4*q)/(math.pi*d*v))
print('%4.f' %rey)