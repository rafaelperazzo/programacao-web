# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')
for i in range (1,n-1,1):
    if n//2==0:
        m=-(i/(i**2))
    else:
        p=(i/(i**2))
    s=m+p
print ('s %.5f' %s)
        
