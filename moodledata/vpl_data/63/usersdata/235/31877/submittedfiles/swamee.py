# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltah=float(input('digite deltah:'))
v=float(input('digite v:'))
g=9.1
e=0.000002
pi=math.pi
d=((8*f*l*(q**2))/((pi**2)*g*deltah))**(1/5)
rey=(4*q)/(pi*d*v)
k=0.25/((math.log10((e/(3.7*d))+(5.74/(rey**0.9))))**2)
print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%f)