# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a>b<c<d and b>a<c<d and c>b<a<d and d>c<b<a and a>b>c>d and b>a>c>d and c>a>b>d and d>a>b>c:
    print('S')
else:
    print('N')
    
