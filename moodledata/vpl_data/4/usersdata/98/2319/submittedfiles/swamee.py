# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
f=input('Digite o valor de f: ')
l=input('Digite o valor de l: ')
q=input('Digite o valor de q: ')
h=input('Digite o valor de h: ')
o=input('Digite o valor de o: ')

g=9.81

d=((8*f*l*(q**2))/((math.pi**2)*g*h))**(1/5)

print(d)