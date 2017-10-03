# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
Delta=b**2-4*a*c
print Delta
 else:
    if Delta >= 0:
    x1 = (-b+Delta**0.5)/2.0*a
    x2 = (-b-Delta**0.5)/2.0*a
    print('%.2f'% x1,'%.2f'%x2)
if Delta < 0:
    print 'SRR'
    