# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('f: ')
L=input('L: ')
Q=input('Q: ')
DeltaH=input('DeltaH: ')
v=input('v: ')

g=9.81
e=0.000002

D=((8*f*L*(Q**2))/((math.pi**2)*g*DeltaH))**(1/5)

rey=(4*Q)/(math.pi*D*v)

k=(0.25)/(math.log10((e/(3.7*D))+((5.74)/rey**0.9)))

print('D=%.4f' %D)
print('rey=%.4f' %rey)
print('k=%.4f' %k)