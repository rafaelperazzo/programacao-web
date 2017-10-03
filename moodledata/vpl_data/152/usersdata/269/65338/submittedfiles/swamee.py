# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('difite f: '))
l=float(input('digite l: '))
q=float(input('digite q: '))
deltah=float(input('digite denta H: '))
v=float(input('digite o valor de v: '))

d= ((8*f*l*q*q)/(math.pi*math.pi*9.81*deltah))**(1/5)

rey= (4*q)/(math.pi*d*v)

k= (0.25)/(math.log10((0.000002/(3.7*d))+5.74/(rey**0.9)))**2

print('%.4f' %d)
print('%.4f' c%rey)
print('%.4f' %k)