# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('Digite o valor:')
L=input('Digite o valor:')
Q=input('Digite o valor:')
DeltaH=input('Digite o valor:')
v=input('Digite o valor:')

g= 9.81
e= 0.000002
pi= 3.14 

D= ((8*f*L*(math.pow(Q,2)))/(math.pow(pi,2)*g*DeltaH))**0.2
Rey= (4*Q)/(pi*D*v)
k= (0.25)/math.pow((math.log10((e/(3.7*D))+(5.74/Rey**0.9))),2)

print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)

