# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

if (a>b and a>c and a>d):
    print('S')
    
if (b>a and b>c and b>d):
    print('S')
    
if (c>a and c>b and c>d):
    print('S')
    
if (d>a and d>b and d>c):
    print('S')
    
else:
    print('N')