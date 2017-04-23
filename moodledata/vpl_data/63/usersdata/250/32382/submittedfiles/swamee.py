# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltah=float(input('digite o delta:'))
v=float(input('digite v:'))
g=9.81
e=0.000002
D=((((8*f*l*q*q)/((math.pi**2)*(g*deltah))))**1/5)
print('o valor de D é:%.4f'%D)
rey=((4*q)/(math.pi*D*v))
print('o valor de rey é:%.4f'%rey)
k=0.25/(math.log10((e/(3.7*D))+(5.74/(rey**0.9))))
print('o valor de k é:%.4f'%k)



