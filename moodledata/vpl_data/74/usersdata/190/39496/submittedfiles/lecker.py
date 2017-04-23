# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
if a>b or b>a or a>c or c>a or a>d or d>a or b>c or c>b or b>d or c>d or d>b or d>c:
    print('S')
else:
    print('N')