# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite a:'))

if a>b>c>d and a<b<c<d and b<a<b<d and b>a>c>d and c>a>b>d and c<a<b<d and c<a<d<b:
    print('S')
else:
    print('N')