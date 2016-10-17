# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
i=a
x=b
c=0
while True:
    if i%x!=0:
        c=c+1
    if i%x==0:
        break
    i=x
    x=i%x
print(c)    