# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
c=input('c:')
d=input('d:')
if a>b and a>c and a>d:
    print ('%f maior' %a)
elif b>a and b>c and b>d:
    print ('%f maior' %b)
elif c>a and c>b and c>d:
    print ('%f maior' %c)
elif d>a and d>b and d>c:
    print ('%f maior' %c)
if a<b and a<c and a<d:
    print ('%f menor' %a)
elif b<a and b<c and b<d:
    print ('%f menor' %b)
elif c<a and c<b and c<d:
    print ('%f menor' %c)
elif d<a and d<b and d<c:
    print ('%f menor' %d)
