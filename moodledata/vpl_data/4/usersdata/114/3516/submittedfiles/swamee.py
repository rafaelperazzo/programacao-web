# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f=input('Digite o valor de f: ')
l=input('Digite o valor de l: ')
q=input('Digite o valor de q: ')
deltah=input('Digite o valor de deltah: ')
v=input('Digite o valor de v: ')

D= ((8*f*l*(q**2)) / ((math.pi**2)*9.81*deltah)**(1/5))
Rey=(4*q)/(math.pi*D*v)
K=0.25/((math.log10((0.000002/(3.7*D)) + (5.74/(Rey**0.9))))**2)

print ('D=%.4f' % D)
print ('Rey=%.4f' % Rey)
print ('K=%.4f' % K)