# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

if (a>b and a>c and a>d) or (b>a and b>c and b>d) or (c>b and c>a and c>d) or (d>b and d>c and d>a): 
    print('S')

else:
    print('N')