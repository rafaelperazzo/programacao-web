# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f = input('Digite o valor de f: ')
L = input('Digite o valor de L: ')
Q = input('Digite o valor de Q: ')
DH = input('Digite o valor de DH: ')
V = input('Digite o valor de V: ')
g = 9.81
E = 0.000002
D = ((8*f*L*((Q)**2))/(((math.pi)**2)*g*DH))**(1/5)
Rey = (4*Q)/(math.pi*D*V)
C = (E/(3.7*D)) + (5.74/(Rey**0.9))
k = (0.25/math.log10(C))**2
print('%.4f' %D)
print('%.4f' %Rey)
print('%.4f' %k)