# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite n:')

j=1
i=0
while n!=0:
    a=n%2
    n=n//2
    i=i+a*j
    j=j*10
print i