# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f= input('f:')
l= input('L:')
Q= input('Q:')
h= input ('H:')
v= input('v:')
g=9.81
e=0.000002
pi=math.pi
a=(8*f*l*(Q**2))
b=((pi**2)*g*h)
D=(a/b)**(0.2)
Rey=(4*Q)/(pi*D*v)
x=e/(3.7*D)
y=5.74/(Rey**0.9)
k=(0.25)/math.log10*((x+y)**2)
print('D: %.4f' %D)
print('Rey: %.4f' %Rey)
print('k: %.4f' %k)