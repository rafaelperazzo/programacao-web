# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
delta=(b**2) - (4*a*c)
if delta>=0:
    raizDelta=(delta)**(0.5)
    x1=(-b+raizDelta)/2
    x2=(-b-raizDelta)/2
    print('%.2f'%x1)
    print('%.2f'%x2)
if delta<0:
    print('SSR')
