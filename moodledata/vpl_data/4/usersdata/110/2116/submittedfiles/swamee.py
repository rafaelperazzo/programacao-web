# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('f= ')
l=('L= ')
q=input('Q= ')
dh=input('DeltaH= ')
V=input('V= ')
g=9.81
e=0.000002
d=((8*f*l*q*q)/(math.pi*math.pi*g*dh))**0.2
rey=(4*q)/(math.pi*d*v)
k=(0.25)/((math.log10(e/(3.7*d)+5.74/(rey**0.9)))**2)
print('D=%.4f' %d)
print('Rey=%.4f'%rey)
print('K=%.4f'%k)
