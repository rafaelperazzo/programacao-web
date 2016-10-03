# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('a'))
b=int(input('b'))
if a>=b:
    c=a
else:
    c=b
while True:
    if a%c==0 and b%c==0:
        break
    else:
        c=c-1
print(c)