# -*- coding: utf-8 -*-
import math
a=int(input('digitite o valor 1:'))
b=int(input('digitite o valor 2:'))
c=int(input('digitite o valor 3:'))
d=int(input('digitite o valor 4:'))
if b>a and b>c and d>c and d>b and d>a:
    print('N')
elif c>d and c>b and a>b and a>c and a>d:
    print('N')
elif b>a and b>c or c>b and c>d:
    print('S')
elif a>b and a>(b>=c) and a>(c>=d): 
    print('S')
elif d>c and d>(c>=b) and d>(b>=a):
    print('S')
else:
    print('N')

    