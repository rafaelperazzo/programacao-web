# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input ('digite o valor de n:')
s=0
i=1
while (i<=n):
    x= ((2*i)-i)/(i**2)
    if i%2==0:
        s=s-x
    else:
        s=s+x
    i=i+1
print('%.5f' %s)
