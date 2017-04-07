# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
delta=(b*b)-(4*a*c)
if delta>=0:
    x1=(-b+delta**0.5)/2*a
    x2=(-b-delta**0.5)/2*a
    print('x1 é igual a:%.2f'%x1)
    print('x2 é igual a:%.2f'%x2)
else delta<=0:
    print('srr')
    
#COMECE A PARTIR DAQUI!
