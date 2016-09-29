# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input ('Digite o valor de f: ')
L = input ('Digite o valor de L: ')
Q = input ('Digite o valor de Q: ')
dh = input ('Digite o valor de delta H: ')
v = input ('Digite o valor de v: ')
E = 0.000002

D = float (8*f*L*(Q**2))/((math.pi**2)*9.81*dh)**0.2
Rey = float (4*Q)/(math.pi*D*v)
K = float (0.25/((math.log10((E/(3.7*D))+(5.74/Rey**(0.9))))**2))


print ("(0:.4f)", D) 
print ("(0:.4f)", Rey)
print ("(0:.4f)", K)
