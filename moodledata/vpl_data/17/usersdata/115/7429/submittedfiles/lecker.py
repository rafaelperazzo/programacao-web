# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o velor de c:')
d=input('digite o valor de d:')

if a>b:
    if c>b and c>d:
        print('N')
    elif d>c:
        print('N')
    elif a==c or a==d:
        print('S')
    else:
        print('N')
elif b>a and b>c:
    if d>c:
        print('N')
    elif b==d:
        print('S')
    else:
        print('S')
elif c>b and c>b:
    print('S')
elif d>c:
    if a==b or a==c or b==c:
        print('S')
    else:
        print('S')
elif a==b or a==c or a==d:
    print('N')
        