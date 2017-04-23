# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a>b+c:
    print('N')
elif a<b+c:
    print('S')
else:
    if a**2==b**2+c**2:
        print()