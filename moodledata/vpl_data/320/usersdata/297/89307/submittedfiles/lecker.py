# -*- coding: utf-8 -*-
import math
a=int(input(' '))
b=int(input(' '))
c=int(input(' '))
d=int(input(' '))
if a>b>=c>=d or a<b>c>=d or a<=b<c>d  or a<=b<=c<d or (a=c>b and d<=a and d<=b ) or (b=d>c and a<=d and a<=c) :
    print('S')
else :
    print('N')