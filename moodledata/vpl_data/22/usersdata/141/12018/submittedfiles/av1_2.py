# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10
d=n/1
if (a==b) or (b==c) or (c==d):
    print('F')
else:
    if (a==c) or (b==d):
        print('V')
else:
   print('F')