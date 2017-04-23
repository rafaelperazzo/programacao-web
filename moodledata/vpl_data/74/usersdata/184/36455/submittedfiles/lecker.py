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
    if a>b or a>c or a>d and b>a or b>c or b>d:
        print('N')
    elif a>b or a>c or a>d and c>a or c>b or c>d:
        print('N')
    elif a>b or a>c or a>d and d>a or d>b or d>c:
        print('N')
    elif b>a or b>c or b>d and c>a or c>b or c>d:
        print('N')
    elif b>a or b>c or b>d and d>a or d>b or d>c:
        print('N')
    elif c>a or c>b or c>d and d>a or d>b or d>c:
        print('N')
    else:
        print('N')