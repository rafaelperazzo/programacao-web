# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
if a>b or a>c or a>d or b>a or c>a or d>a and b<=c<=d:
    print('S')
elif b>a or b>c or b>d or a>b or c>b or d>b and a<=c<=d:
    print('S')
elif c>a or c>b or c>d or a>c or b>c or d>c and a<=b<=d:
    print('S')
elif d>a or d>b or d>c or a>d or b>d or c>d and a<=b<=c:
    print('S')
else:
    print('N')