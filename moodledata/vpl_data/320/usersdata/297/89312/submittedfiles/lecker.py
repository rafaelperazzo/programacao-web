# -*- coding: utf-8 -*-
import math
a=int(input(' '))
b=int(input(' '))
c=int(input(' '))
d=int(input(' '))
if a>b>=c>=d or a<b>c>=d or a<=b<c>d  or a<=b<=c<d or (a>b<c<=d and a==c) :
    print('S')
else :
    print('N')