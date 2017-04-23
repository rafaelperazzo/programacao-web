# -*- coding: utf-8 -*-
import math
a=int(input('digite v1'))
b=int(input('digite v2:'))
c=int(input('digite v3:'))
d=int(input('digite v4:'))

if (b>a) and (b>c) and (d>c) and (d>b) and (d>a):
    print('N')
elif (c>d) and (c>b) and (a>b) and (a>c) and (a>d):
    print('N')
elif (b>a) and (b>c) or (c>b) and (c>d):
    print('S')
elif (a>b) and (d>a) or (d>c) and (a>b):
    print('N')
elif (a>b) or (d>c):
    print('S')
elif (a>b) and (b>=c) and (c>=d):
    print('S')
elif (d>c) and (c>=b) and (b>=a):
    print('S')
else:
    print('N')