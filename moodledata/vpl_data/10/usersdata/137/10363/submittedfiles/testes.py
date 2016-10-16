# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
c=input('c:')
d=input('d:')
if a>b and a>c and a>d:
    maior=a
elif b>a and b>c and b>d:
    maior=a
elif c>a and c>b and c>d:
    maior=c
elif d>a and d>b and d>c:
    maior=d
elif a<b and a<c and a<d:
    menor=a
elif b<a and b<c and b<d:
    menor=b
elif c<a and c<b and c<d:
    menor=c
elif d<a and d<b and d<c:
    menor=d
print ('%d,%d' %(menor,maior))
