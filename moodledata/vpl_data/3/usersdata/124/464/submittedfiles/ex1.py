# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite o valor de a: ')
b = input('Digite o valor de b: ')
c = input('Digite o valor de c: ')
delta = b**2 - (4*a*c)
R1 = (-b+delta**0.5)/2*a
R2 = (-b-delta**0.5)/2*a

if delta<0:
    print('A equação não tem raízes reais')
else:
    print('O valor da primeira raíz é: %.2f' %R1)
    print('O valor da segunda raíz é: %.2f' %R2)