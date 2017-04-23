# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
d=float(input('digite o valor de d:'))
if a>b or b>c or c>d or b>a or c>b or d>c:
    print('S')
else:
    if a>b and b>c or b>a and b>c or c>b and c>d:
        print('N')