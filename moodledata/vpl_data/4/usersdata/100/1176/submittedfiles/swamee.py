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
D = (((q**2)*8*l*f)/((math.pi**2)*g*deltah))**(1/5)
Rey = (4Q)/(math.pi*D*v)
k= 0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9)))**2
print D
print Rey
print k