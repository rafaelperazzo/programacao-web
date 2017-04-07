# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('Digite a: '))
b=float(input('Digite b: '))
c=float(input('Digite c: '))
delta=(b**2)-4*a*b
raizdelta=delta**0.5
if raizdelta>=0:
    x1=(-b+raizdelta)/(2*a)
    x2=(-b-raizdelta)/(2*a)
    print('%.2f'%x1)
    print('%.2f'%x2)
else:
    print('srr')

        
