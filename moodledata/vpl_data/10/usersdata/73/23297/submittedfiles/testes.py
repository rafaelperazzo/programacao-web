# -*- coding: utf-8 -*-
from __future__ import division

n=input('n')
s=0
for i in range (1,n+2,1):
    if i%2==1:
        s=s+i
    else:
        s=s+(1/i)
print s