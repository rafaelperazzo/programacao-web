# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite o delta:'))
v=float(input('digite v:'))
d=((8*f*l*q*q)/(math.pi**2)*9.81*deltaH)**(1/5)
rey=(4*q)/(math.pi*d*v)
k=0.25/[math.log10(0.000002/3.7*d+(5.74/rey**0.9))](**2)
print('valor d %.4f' %d)
print('valor rey %.4f' %rey)
print('valor k %.4f' %k)