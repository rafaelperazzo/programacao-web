# -*- coding: utf-8 -*-
import math
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>(b+c+d) or b>(a+c+d) or c>(b+a+d) or d>(b+c+a):
    print('S')
else: print('N')