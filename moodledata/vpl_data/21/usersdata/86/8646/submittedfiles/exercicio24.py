# -*- coding: utf-8 -*-
from __future__ import division
import math
a = int(input('a:')
b = int(input('b:')
if a>=b:
    x=b
else:
    x=a
while True:
    if a%x==0 and b%x==0:
        print (x)
        break
    elif a%x!=0 or b%x!=0:
        x=x-1
    if x==1:
        print(x)
