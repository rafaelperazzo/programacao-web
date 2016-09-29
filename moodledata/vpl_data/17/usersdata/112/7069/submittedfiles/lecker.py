# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('digite o valor de d:')
if (a>b and a>c and a>d) or (b>a and b>c and b>d) or (c>a and c>b and c>d) or (d>a and d>b and d>c):
    print('S')
if a==b==c==d:
    print('N')