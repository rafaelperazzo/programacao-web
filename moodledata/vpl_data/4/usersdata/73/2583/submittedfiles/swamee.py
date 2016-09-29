# -*- coding: utf-8 -*-
from __future__ import division
import math
f = input ('digite f:')
L = input ('digite l:')
Q = input ('digite q:')
dH = input ('digite dH:')
v = input 'digite v'
g = 9.81
e = 0.000002
d =(((8*f*L*(Q**2)))/((math.pi**2)*g*dH))**(0.2)
rey = ((4*Q)/(math.pi*d*v))
k = 0.25 /(math.log10((e/(3.7*d)+(5.74/(rey**0.9)))))**2
print 'D = %.4f'%d
print 'Rey = %.4f'%rey
print 'K = %.4f'%k