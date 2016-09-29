# -*- coding: utf-8 -*-
from __future__ import division
import math

#entrada
f = input('digite um valor para f:')
L = input('digite um valor para L:')
Q = input('digite um valor para Q:')
dH = input('digite um valor para dH:')
v = input('digite um valor para v:')
#processamento
g = 9.81
E = 0.000002

D = (((8*f*L*(Q**2))/((math.pi**2)*g*dH)))**0.2
Rey = (4*Q)/(math.pi*D*v)
k = ((0.25)/(math.log10((E/(3.7*D))+(5.74/(Rey**0.9))))**2)
#saida
print('D=%4.f' %D)
print('Rey=%4.f' %Rey)
print('k=%4.f' %k)