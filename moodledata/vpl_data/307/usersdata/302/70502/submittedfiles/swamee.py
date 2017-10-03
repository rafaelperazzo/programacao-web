# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f = float(input('Digite f '))
l = float(input('Digite l '))
q = float(input('Digite q '))
h = float(input('Digite h '))
v = float(input('Digite v '))
g=(9.81)
e=(0.000002)
d=(((8*f*l*(q**2))/(math.pi)**2*g*h)**0.2)
print ('%.4f' %d)
rey=((4*q)/(math.pi)*d*v)
print ('%.4f' %rey)
k=(0.25/(math.log((e/3.7*d)+(5.73/rey**0.9))**2))
print('%f'%k)