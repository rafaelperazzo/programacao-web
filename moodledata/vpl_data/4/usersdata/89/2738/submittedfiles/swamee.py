# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('Digite o valor de f: ')
L=input('Digite o valor de L: ')
Q=input('Digite o valor de Q: ')
deltaH=input('Digite o valor de deltaH: ')
v=input('Digite o valor de v: ')

g=(9.81)
e=(0.000002)

D=((8*f*L*(Q**2))/float((math.pi**2)*g*deltaH)**(0.2))
Rey=((4*Q)/float(math.pi*D*v))
k=(((0.25)/float(math.log10((e/3.7*D)+(5.74*(Rey**0.9))))**2))

print(D)
print(Rey)
print(k)