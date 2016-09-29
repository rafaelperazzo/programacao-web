# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('digite o valor de d:')
if (a>b and c and d) or (b>a and c and d) or (c>a and b and c) or (d>a and b and c):
    print('S')
if a==b or a==c or a==d:
    print('N')
if a==b or b==c or b==d:
    print('N')
if c==b or a==c or c==d:
    print('N')
if d==b or d==c or a==d:
    print('N')