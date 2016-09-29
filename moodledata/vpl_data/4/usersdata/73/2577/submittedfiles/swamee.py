# -*- coding: utf-8 -*-
from __future__ import division
import math
f = input ('digite f:')
L = input ('digite l:')
Q = input ('digite q:')
dH = input ('digite dH:')
V = input ('digite V:')
d=(((8*f*L*(Q*Q)))/(((math.pi**2)*9.81*dH))**(0.2)
rey = ((4*Q)/(math.pi*d*V))
k=0.25/(math.log10((0.000002/(3.7*d) + (5.74/(rey**0.9)))))**2
print ('D=%.4f' %d)
print ('Rey=%.4f' %rey)
print ('K=%.4f'%k)

