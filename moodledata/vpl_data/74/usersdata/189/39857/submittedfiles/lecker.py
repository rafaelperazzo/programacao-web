# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a>b:
    if c>b and c>d or d>c:
        print('N')
    else:
        print('S')
elif b>a and b>c:
    if c>b and c>d or d>c:
        print('N')
    else:
        print('S')
elif c>b and c>d:
    if a>b:
    print('N')
elif d>c:
    if b>a and b>c:
        print('N')
    else:
        print('S')
else:
    print('N')