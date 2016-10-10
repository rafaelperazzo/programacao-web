# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
r=int(a%b)
while r!=0:
    a=b
    b=r
    r=a%b
print (b)
