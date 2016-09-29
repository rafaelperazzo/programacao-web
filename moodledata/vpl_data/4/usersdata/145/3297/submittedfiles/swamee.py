# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f=input('digite um valor de f:')
l=input('digite um valor de l:')
Q=input('digite um valor de Q:')
deltaH=input('digite um valor de deltaH:')
v=input('digite um valor de v:')

#processamento
g=(9,81)
e=(0,000002)
D=((8*f*l*(Q**2))/((math.pi**2)*g*deltaH))**2
Rey=((4*Q)/(math.pi*D*v))
k=0.25/(math.log10((e/(3.7*D))+(5.74/(Rey**(0.9))**2

#saida

print('D=%.4F'%D)
print('Rey=%.4F'%Rey)
print('k=%.4F'%k)