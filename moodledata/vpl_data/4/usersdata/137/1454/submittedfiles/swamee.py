# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f= input('f:')
l= input('L:')
q= input('Q:')
h= input ('H:')
v= input('v:')
g=9.81
e=0.000002
pi=3.14159265359
D=(((8*f*l*(q**2))/((pi**2)*g*h)))**(0.2))
Rey= ((4*q)/(pi*D*v))
k= (0.25)/((math.log10((e/(3.7*D))+(5.74/(Rey**0.9)))))**2)
print('D: %.4f' %D)
print('Rey: %.4f' %Rey)
print('k: %.4f' %k)