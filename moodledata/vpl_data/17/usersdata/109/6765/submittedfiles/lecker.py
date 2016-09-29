# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')

if a>b and c<b and d<b:
    print 'S'
elif b>a and c<a and d<=c:
    print'S'
elif b>c and a<c b<=a:
    print'S'
elif c>d and b<d and a<=b:
    print 'S'
elif c>b and d<b and a<=b:
    print 'S'
elif d>c and b<c and a<=b:
    print 'S'
else:
    print 'N'