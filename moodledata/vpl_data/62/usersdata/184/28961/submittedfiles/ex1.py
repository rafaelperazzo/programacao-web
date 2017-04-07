# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
Delta = (b*b)-(4*a*c)
if Delta>=0:
 x1=(-b+Delta**0.5)/(2*a)
 x2=(-b-Delta**0.5)/(2*a)
 print('o valor de x1 é:%f'%x1)
 print('o valor de x2 é:%f'%x2)
else:
    print('SRR')