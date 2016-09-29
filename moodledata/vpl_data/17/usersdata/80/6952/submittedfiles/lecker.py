# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o primeiro numero:'))
b=int(input('digite o segundo numero:'))
c=int(input('digite o terceiro numero:'))
d=int(input('digite o quarto numero:'))

if a>b and b>=c and c>=d:
    print('S')
elif a<b and b>c and c>=d:
    print('S')
elif a<=b and b<c and c>d:
    print('S')
elif a<=b and b<=c and c<d:
    print('S')
elif a==b and a==d and c>a:
    print ('S')
elif a==c and a==d and b>a:
    print ('S')
elif a==b and a==d and d>a:
    print ('S')
elif b==c and b==d and a>b:
    print ('S')
else:
    print('N')
    