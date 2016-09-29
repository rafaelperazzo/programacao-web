# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de p1: ')
b=input('Digite o valor de c1: ')
c=input('Digite o valor de p2: ')
d=input('Digite o valor de c2: ')

if a*b>c*d:
    print '-1'
if c*d>a*b:
    print '1'
if a*b==c*d:
    print '0'