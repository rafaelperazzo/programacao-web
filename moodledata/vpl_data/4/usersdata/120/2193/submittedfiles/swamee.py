# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
f=input('Digite o valor de f:')
l=input('Digite o valor de l:')
q=input('Digite o valor de q:')
deltah=input('Digite o valor de deltah:')
v=input('Digite o valor de v:')

#PROCESSAMENTO
d=((8*f*l*(q**2))/((math.pi**2)*9.81*deltah))**0.2

rey=(4*q)/(math.pi*d*v)

k=(0.25)/(math.log10((0.000002/(3.7*d))+(5.74/(rey**0.9)))**2)

#SAIDA
print('d=%.4f'%d)
print('rey=%.4f'%rey)
print('k=%.4f'%k)
