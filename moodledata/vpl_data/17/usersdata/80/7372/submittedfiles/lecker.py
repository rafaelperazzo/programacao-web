# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o primeiro numero:'))
b=int(input('digite o segundo numero:'))
c=int(input('digite o terceiro numero:'))
d=int(input('digite o quarto numero:'))

if a>b and b>=c and c>=d:
    print ('S')
elif a>b and b<c and c==d:
    print ('S')
elif a<b and b>c and c>=d:
    print ('S')
elif c>d and c>b and b>=a:
    print ('S')
elif d>c and c>=b and b>=a:
    print ('S')
elif d>c and c<b and b==a:
    print ('S')
else:
    print('N')