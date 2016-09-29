# -*- coding: utf-8 -*-
from __future__ import division
import math

f=input('Digite o valor de f:')
l=input('Digite o valor de l:')
q=input('Digite o valor de q:')
deltah=input('Digite o valor de deltah:')
v=input('Digite o valor de v:')

d=((8*f*l*(q**2))/((3.1415**2)*9.81*deltah))**1/5.0

rey=(4*q)/(3.1415*d*v)

k=(0.25)/((math.log10((0.000002)/(3.7*d)+(5.74)/(rey**0.9))**2

print('Seu valor de d%.4f:' %d)
print('Seu valor de rey%.4f:'%rey)
print('Seu valor de k%.4f:'%k)