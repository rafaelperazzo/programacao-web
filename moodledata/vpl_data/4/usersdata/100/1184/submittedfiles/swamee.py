# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f = input ('digite f:')
l = input ('digite L:')
q = input ('digite Q:')
deltah=input ('digite delta H:')
v= input ('digite v:')
g=9.81
e=0.000002
d=(((8*f*l(q**2)))/((math.pi**2)*g*deltah))**(0.2)
rey=((4*q)/(math.pi*d*v))
k=0.25/(math.log10((e/(3.7*d)+(5.74/(rey**0.9)))))**2
print ('%.4f'%k)
print ('%.4f'%rey)
print ('%.4f'%d)