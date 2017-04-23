# -*- coding: utf-8 -*-
import math
a=float(input('digite um numero:'))
b=float(input('digite um numero:'))
c=float(input('digite um numero:'))
d=float(input('digite um numero:'))
if a!=b!=c!=d:
    if a<b>c and d<c:
        print('S')
    elif  b<c>d  and a<b:
        print('S')
    elif a>b and c<b and d<b:
        print('S')
    elif d>c and a<c and b<c:
        print('S')
else:
    print('N')
