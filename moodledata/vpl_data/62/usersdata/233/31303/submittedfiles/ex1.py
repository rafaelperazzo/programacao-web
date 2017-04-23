# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta=(b**2)-4*a*c
x1=(-b+Delta**(1/2))/2*a
x2=(-b-Delta**(1/2))/2*a
If Delta>0:
    print('x1: %.2f'%x1)
    print('x2: %.2f'%x2)
Elif Delta=0:
    print(X