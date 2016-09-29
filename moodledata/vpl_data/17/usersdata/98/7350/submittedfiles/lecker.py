# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
c=input('Digite o valor de c: ')
d=input('Digite o valor de d: ')

if a==b==c==d:
    print ('N')
elif c>b and c>d and a>b:
    print ('N')
elif a>b and d>c:
    print ('N')
elif b>a and b>c and d>c:
    print ('N')
elif b>c and b==c and c>d:
    print ('N')
else:
    print ('S')
