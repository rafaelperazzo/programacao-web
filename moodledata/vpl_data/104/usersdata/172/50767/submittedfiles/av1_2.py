# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
x1=int(input('digite x1: '))
y1=int(input('digite y1: '))
x2=int(input('digite x2: '))
y2=int(input('digite y2: '))
a=x1+y1
b=x2+y2
c=n/2
if x1==x2:
    if y1<=c and y2>c:
        print('S')
    elif y1>c and y2<=c:
        print('S')
    else:
        print('N')
elif y1==y2:
    
    