# -*- coding: utf-8 -*-
from __future__ import division
n=100
b=0
for i in range(0,n-1,1):
    if n%(i+1)!=0:
        b=b+1
print(b)