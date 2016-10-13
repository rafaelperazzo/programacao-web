# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('n: '))
s=0
for i in range(1,n+1,1):
    s=s+i/(n-i+1)
print(s)