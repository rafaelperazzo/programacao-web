# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor 1: '))
b=int(input('digite o valor 2: '))
c=int(input('digite o valor 3: '))

if b>a and b>c or c>b and c>d:
    print('S')
elif a>b and b>=c and c>=d:
    print('S')
elif d>c and c>=b and b>=a:
    print('S')
else:
    print('N')
