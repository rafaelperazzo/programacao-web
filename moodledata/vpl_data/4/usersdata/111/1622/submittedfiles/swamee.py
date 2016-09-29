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

numeradorded=(8*f*l*(q**2))
denominadorded=(((math.pi)**2)*g*h)


D=((numeradorded)**0.2)/((denominadorded)**0.2)

rey=(4*q)/(math.pi*D*v)

x=((e)/(3.7*D)) + ((5.74)/(rey**0.9))

k=(0.25)/(math.log10(x)**2)

print(' O valor de D é %.4f ' %D)

print(' O valor de Rey é %.4f ' %rey)

print(' O valor de k é %.4f ' %k)
