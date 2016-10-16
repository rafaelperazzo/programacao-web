# -*- coding: utf-8 -*-
from __future__ import division
import math

N=int(input('Digite o N:'))
if N<0:
 N=N*(-1)

t=0
for i in range (0, N, 1):
    t = t +((i+1)/(N-i))
print ('%.5f' %t)