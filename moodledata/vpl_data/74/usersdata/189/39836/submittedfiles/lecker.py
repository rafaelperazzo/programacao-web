# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a>b>c>d:
    print('S')
    if a<b>c<d:
        print('S')
    if c>a>=b>=d:
        print('S')
    if d>a>=b>=c:
        print('S')
else:
    print('N')