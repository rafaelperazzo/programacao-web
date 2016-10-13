# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite o número:'))
i=1
c=0
while True:
    if n//i!=0:
        c=c+1
    break    
    i=i*10
print(c)    