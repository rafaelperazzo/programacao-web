# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Digite n:'))
if n<0:
    n=n*(-1)
S=0
for i in range (0,n,1):
    S=S+((i+1)/(n-1))
print ('%.5f' %S)
