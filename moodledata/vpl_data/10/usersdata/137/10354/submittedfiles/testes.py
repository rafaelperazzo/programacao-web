# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
c=input('c:')
d=input('d:')
if a>b>c>d:
    print (a)
elif b>a>c>d:
    print (b)
elif c>b>a>d:
    print (c)
elif d>a>b>c:
    print (d)
elif a<b<c<d:
    print (a)
elif b<a<c<d:
    print (b)
elif a<b<a<d:
    print (c)
else: 
    print(d)