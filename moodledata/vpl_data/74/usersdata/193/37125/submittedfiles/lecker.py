# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor 1:'))
b=int(input('digite o valor 2:'))
c=int(input('digite o valor 3:'))
d=int(input('digite o valor 4:'))

if b>a and b>c and d>c:
    print('N')
elif c>d and c>b and a>b:
    print('N')
elif b>a and b>c or c>b and c>d:
    print('S')
elif a>b and d>c:
    print('N')
elif a>b or d>c:
    print('S')
else:
    print('N')
