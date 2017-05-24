# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
x1=int(input('digite x1:'))
y1=int(input('digite y1:'))
x2=int(input('digite x2:'))
y2=int(input('digite y2:'))
z=n/2
if x1<=z and x2>z or y1<=z and y2>z:
    print('s')
else:
    print('N')

