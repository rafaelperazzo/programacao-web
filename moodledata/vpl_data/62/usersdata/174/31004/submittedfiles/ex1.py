# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
Delta = (b**2)-4*a*c
x1 = (-(b**2)+(Delta**0.5))/(2*a)
x2 = (-(b**2)-(Delta**0.5))/(2*a)
if Delta>=0:
    print('%.2f' %x1)
    print('%.2f' %x2)
else:
    print('SRR')