# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')

d=((b**2)-(4*a*c))**1/2
x1=(-b+d)/2*a
x2=(-b-d)/2*a

if d>=0:
print('Valor de x1 é: %.1f' %x1)
print('valor de x2 é: %.1f' %x2)

