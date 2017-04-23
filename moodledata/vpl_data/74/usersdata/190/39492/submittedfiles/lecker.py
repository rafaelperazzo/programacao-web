# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
if a>b or b>a or b>c or c>b or c>d or d>c and a!=b!=c!=d:
    print('S')
else:
    print('N')