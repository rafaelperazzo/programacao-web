# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input ('insira o valor de f:') 
L = input ('insira o valor de L:')
Q = input ('insira o valor da Q:') 
DeltaH = input ('insira o valor de DeltaH:') 
v = input ('insira o valor de v:') 

g = 9.81
E = 0.000002 
D = (8*f*L*Q*Q)/(((math.pi**2)*g*DeltaH)**(1/5))
Rey = (4*Q)/((math.pi**2)*D*v) 
k=0
#k = (0.25)/(math.log10((E/(3.7*D)+((5.74)/(Rey))**(0.9))**(0.5))

print ("%.3f" % k)
