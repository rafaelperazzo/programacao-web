# -*- coding: utf-8 -*-
from __future__ import division
import math


f=input('digite o valor de f:')
L=input('digite o valor de L:')
Q=input('digite o valor de Q:')
dh=input('digite o valor de dh:')
v=input('digite o valor de v:')

g=9.81
E=0.000002

D=((8*f*L*Q**2)/(dh*9.81*3.14**2))**(1.0/5)
Rey= 4*Q/(3.14*D*v)

k=0.25/(math.log10(E/(3.7*D)+5.74/(Rey**0.9))**2)

print 'o valor de D=%.4f'%D
print 'o valor de Rey=%.4f'%Rey
print 'o valor de k=%.4f'%k
