# -*- coding: utf-8 -*-
from __future__ import division
a=input(int('Digite a: '))
b=input(int('Digite b: '))
c=input(int('Digite c: '))
Delta=(b**2)-(4*a*c)
if Delta>=0:
    x1=(-b+Delta**(1/2))/(2*a)
    x2=(-b-Delta**(1/2))/(2*a)
    print('x1:%.2f'%x1)
    print('x2:%.2f'%x2)
else:    
    print(SRR)
