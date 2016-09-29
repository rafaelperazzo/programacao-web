# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('digite o valor de d:')

if a<b and b>c and c<d:
    print('N')
if a>b and b>c and c<d:
    print('N')
if a>b and b<c and c<d:
    print('N')
else:
    print('S')