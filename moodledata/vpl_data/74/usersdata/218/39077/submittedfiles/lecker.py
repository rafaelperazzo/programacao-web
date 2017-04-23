# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
if a>b:
    if b>a or b>c or c>b or c>d or d>c:
        print('N')
    else:
        print('S')
elif b>a and b>c:
    if c>b or a>b or c>b or c>d or d>c:
        print('N')
    else:
        print('S')
if c>b and c>d:
    if b>a or b>c or c>b or c>d or d>c:
        print('S')        