# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input ('digite o valor de a:')
b=input ('digite o valor de b:')
c=input ('digite o valor de c:')
d=input ('digite o valor de d:')

if a>b and a<b>c:
    print ('N')
elif a>b and b<c>d:
    print ('N')
elif a>b and c<d:
    print ('N')
elif a<b>c and b<c>d:
    print ('N')
elif a<b>c and c<d:
    print ('N')
elif b<c>d and c<d:
    print ('N')
else:
    print ('S')