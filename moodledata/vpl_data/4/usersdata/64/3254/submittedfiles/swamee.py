# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

f = input('Digite o valor de f: ')
L = input('Digite o valor de L: ')
Q = input('Digite o valor de Q: ')
DH = input('Digite o valor de DeltaH: ')
V = input('Digite o valor de V: ')
g = 9.8
E = 0.000002

#PROCESSAMENTO

D = ((8**L(Q**2.0))/((math.pi**2.0)*g*DH))**(1/5.0) 
Rey = (4*Q)/((math.pi)*D*V)
k = 0.25/((math.log((E/(3.7*D)) + (5.74/Rey**(0.9))))**2)

#SAÍDA

print('D=%.4f' %(D))
print('Rey=%.4f' %(Rey))
print('k=%.4f' %(k))

