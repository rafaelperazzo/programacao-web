# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('digite o valor de d:')
if a>b and a>c and a>d:
    print('S')
if b>a and b>c and b>d:
    print('S')
if c>b and c>a and c>d:
    print('S')
if d>b and d>c and d>a:
    print('S')
elif a>b and b>=c and c>=d:
    print('S')
elif a<b and b>c and c>=d:
    print('S')
elif a<=b and b<=c and c>d:
    print('S')
elif a<=b and b>=c and c<d:
    print('S')
elif a<b and b>c and c<d:
    print('N')
elif a>b and b>c and c<d:
    print('N')
elif a>b and b<c and c<d:
    print('N')
else:
    print('N')