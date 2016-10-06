# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite a quantidade de termos:')
i=1
s=0
while i<=n:
    if i%2!=0:
        s=(i/(i**2))+s
        i=i+1
    else:
        s=(-i/(i**2))+s
        i=i+1
print ('%.5f' %s)
