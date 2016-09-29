# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

f=input('Digite o valor de f: ')
l=input('Digite o valor de L: ')
q=input('Digite o valor de Q: ')
h=input('Digite o valor de delta H: ')
v=input('Digite o valor de v: ')

g=9.81
e=0.000002


D=(8*f*l*q**2)/(5**2*g*h)**0.2

rey=(4*q)/(5*D*v)

k=(0.25)/(5*((e)/(3.7*D) + (5.74)/(rey**0.9))**2

print(' o valor de D é %.4f ' %D)

print(' o valor de Rey é %.4f ' %rey)

print(' o valor de k é %.4f ' %k)

