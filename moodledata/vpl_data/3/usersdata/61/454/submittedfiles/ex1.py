# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite um número: ')
b=input('Digite um número: ')
c=input('Digite um número: ')
DELTA=b**2 - (4*a*c)
x1=((-b)+DELTA**0.5)/(2*a)
x2=((-b)-DELTA**0.5)/(2*a)

if DELTA>=0:
    print('%.2f' %x1)
    print('%.2f' %x2)
else:
    print('A equação não possui raiz real')
    
    

