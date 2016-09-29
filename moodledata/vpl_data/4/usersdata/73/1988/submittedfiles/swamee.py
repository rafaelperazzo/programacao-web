# -*- coding: utf-8 -*-
from __future__ import division
import math
f = input ('digite f:')
L = input ('digite l:')
Q = input ('digite q:')
dH = input ('digite dH:')
V = input ('digite V:')

D=((8*f*L(Q**2))/((math.pi**2)*9.81*dH)**0.2
print ('D=%.4f' %D)
Rey=(4*Q)/(math.pi*D*V)
print ('Rey=%.4f' %Rey)
K=0.25/(math.log10((0.000002/(3.7*D)) + (5.74/(Rey**0.9)))**2
print ('K=%.4f'%K)

