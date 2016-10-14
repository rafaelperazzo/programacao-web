# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite n:'))
if n<0:
 n=n*(-1)

s=0
for i in range (0, n, 1):
    s = s +((i+1)/(n-i))
print ('%.5f' %s)
