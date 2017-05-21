# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite n:'))
resto=n%2
i=0
s=0
for i in range (1,n+1,1):
    i%2==0
    s=s+resto*10**i
    n=n//2
print(s)