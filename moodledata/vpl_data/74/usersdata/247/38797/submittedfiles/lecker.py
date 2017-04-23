# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
if a>b and b<=c and d<=c and c<=d:
    print('S')
elif b>a and b>c and d<=c:
    print('S')
elif a<=b and c>b and c>d:
    print('S')
elif c>=b and b>=a and d>c:
    print('S')
else:
    print('N')