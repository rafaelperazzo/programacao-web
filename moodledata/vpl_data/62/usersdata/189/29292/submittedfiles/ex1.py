# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
delta=(b*b)-(4*a*c)
if delta>=0:
    x1=(-b+delta**(1/2))/(2*a)
    x2=(-b-delta**(1/2))/(2*a)
    print('%f' %x1)
    print('%f' %x2)
else:print('Não existe raizes reais')
