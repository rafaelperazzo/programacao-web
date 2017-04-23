# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
d=float(input('digite o valor de d:'))
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