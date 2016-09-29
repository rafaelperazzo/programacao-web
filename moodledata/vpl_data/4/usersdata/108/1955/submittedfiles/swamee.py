# -*- coding: utf-8 -*-
from __future__ import division
import math

f = input ('Digite f:')
L = input ('Digite L:')
Q = input ('Digite Q:')
dH = input ('Digite delta H:')
T = input ('Digite de teta:')

g = 9.81
e = 0.000002


D = ((8*f*L*(Q**2))/((math.pi**2)*g*dH))**(1/5)
Rey = (4*Q)/(math.pi*D*t)
k = 0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**0.9))))**2

print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)
