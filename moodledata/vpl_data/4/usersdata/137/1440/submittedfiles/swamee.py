# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f= input('f:')
l= input('L:')
q= input('Q:')
DH= input('DH:')
O= input('O:')
g=9.81
e=0.000002
pi=3.14159265359
D=((8*f*l*(q**2))/((pi**2)*g*DH))**(1/5)
Rey= ((4*q)/(pi*D*O))
k= ((0.25)/(math.log10*(e/(3.7*D)+((5.74/(Rey**0.9)))**2)
print('%4f' %D)
print('%4f' %Rey)
print('%4f' %k)