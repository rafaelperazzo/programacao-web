# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('informe o valor de a:')
b=input('informe o valor de b:')
c=input('informe o valor de c:')
d=input('informe o valor de d:')
if (a>b) and (b<c) and (c<d):
    print('S')
if (b>a) and (b>c) and (c<d):
    print('S')
if (c>b) and (c>d) and (a<b):
    print('S')
if (a<b) and (b<c) and (c<d):
    print('S')
else:
    print('N')