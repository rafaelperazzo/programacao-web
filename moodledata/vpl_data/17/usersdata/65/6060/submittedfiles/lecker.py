# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

if (a>b):
    print('S')
else:
    print('N')
    
if (b>a and b>c):
    print('S')
else:
    print('N')
    
if (c>b and c>d):
    print('S')
else:
    print('N')
    
if (d>c):
    print('S')
else:
    print('N')