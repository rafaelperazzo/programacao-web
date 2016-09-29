# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite o valor de a: ')
b = input('Digite o valor de b: ')
c = input('Digite o valor de c: ')

if a>b and a>c:
    print('%.2f' %a)
if b>a and b>c:
    print('%.2f' %b)
if c>a and c>b:
    print('%.2f' %c)