# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o peso de A: ')
b = input('Digite o peso de B: ')
c = input('Digite o peso de C: ')
d = input('Digite o peso de D: ')

if (a==b+c+d) and (b+c==d) and (b==c):
    print('S')
else:
    print('N')
    
    
    