# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
if a>b and (b>=c or b<=c) and c>=d:
    print('S')
elif  b>a and b>c and c>=d:
        print('S')
elif  c>b and c>d and b>=a:
        print('S')
elif  d>c and d>b and d>=a:
        print('S')
else:
    print('N')