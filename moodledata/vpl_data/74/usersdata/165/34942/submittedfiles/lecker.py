# -*- coding: utf-8 -*-
import math
a=float(input('digite um numero:'))
b=float(input('digite um numero:'))
c=float(input('digite um numero:'))
d=float(input('digite um numero:'))
if a!=b!=c!=d:
    if a>b and a>c and a>d:
        print('S')
    elif b>a and b>c and b>d:
        print('S')
    elif c>a and c>b and c>d:
        print('S')
    elif d>a and d>b and d>c:
        print('S')
else:
    print('N')
