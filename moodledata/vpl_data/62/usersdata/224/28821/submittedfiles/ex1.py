# -*- coding: utf-8 -*-
from __future__ import division
a =float(input('Digite a: '))
b =float(input('Digite b: '))
c =float(input('Digite c: '))
DELTA=(b*b)-(4*a*c)
print('DELTA')
if Delta>=0:
    x1=(-b-DELTA**(1/2))/(2*a)
    x2=(-b+DELTA**(1/2))/(2*a)
    print('O valor de x1 é: %f'%x1)
    print('O valor de x2 é: %f'%x2)
else:
    print('SRR')
