# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')
a=[1]
for i in range(1,n,1):
    a.append(a[i-1]+i+1)
print(a)