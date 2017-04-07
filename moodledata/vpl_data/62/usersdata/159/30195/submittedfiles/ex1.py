# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = floart(input('Digite c: '))

Delta=(b*b)-(4*a*c)
if Delta>=0:
    x1=((-b)+(Delta**(0.5)))/(2*a)
    x2=((-b)-(Delta**(0.5)))/(2*a)
    print('x1=%.2f' %x1)
    print('x2=%.2f' %x2)
else:
    print('SRR')
