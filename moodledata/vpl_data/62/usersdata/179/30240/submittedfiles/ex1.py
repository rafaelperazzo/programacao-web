# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
delta=(-b**2)-4*a*c
x1=-b+math.sqrt(delta)/2*a
x2=-b-math.sqrt(delta)/2*a
if delta<0 :
    print('SRR')
else :
    print(x1)
    print(x2)
