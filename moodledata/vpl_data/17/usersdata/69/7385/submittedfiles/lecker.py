# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')
if a>b and c>b and c>d:
    print('N')
elif a>b and d>c:
    print('N')
elif a<b and b>c and d>c:
    print ('N')
elif a==b==c==d:
    print ('N')
else:
    print('S')