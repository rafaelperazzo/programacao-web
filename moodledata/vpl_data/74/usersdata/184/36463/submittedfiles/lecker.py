# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
d=float(input('digite o valor de d:'))
if a>b and b<c and c<=d:
    print('S')
elif b>a and b>c and c<=d:
    print('S')
elif c>b and c>d and a<=b:
    print('S')
elif d>c and b>=c and a>=b:
    print('S')
else:
    print('N')