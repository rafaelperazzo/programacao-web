# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
if (a>b or a>c or a>d and b<=c<=d) or (b>a or b>c or b>d and a<=c<=d) or (c>a or c>b or c>d and a<=b<=d) or (d>a or d>b or d>c and a<=b<=c):
    print('S')
else:
    print('N')