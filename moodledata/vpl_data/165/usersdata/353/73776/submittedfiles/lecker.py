# -*- coding: utf-8 -*-
import math
a=int(input('A:'))
b=int(input('B:'))
c=int(input('C:'))
d=int(input('D:'))

if a>b and b>c and c>d:
    print('S')
elif a>b and b==c==d:
    print('S')
elif a>b and a==c==d:
    print('S')
elif d>c and c>b and b>a:
    print('S')
elif d>c and c==b==a:
    print('S')
elif d>c and d==b==a:
    print('S')
elif b>a and b>c and c>a and d<a:
    print('S')
elif b>a and b>c and c>a and a==d:
    print('S')
elif c>a and a==b==d:
    print('S')
else: 
    print('N')
    