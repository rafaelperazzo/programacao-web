# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('insira n:'))

i=1
s=0

while n>=1: 
    if n>0:
        s=(i/n)+s
        n=n-1
        i=i+1
    if n<0:
        s=(i/(-n))+s
        n=(-n-1)
        i=i+1
    if n==0:
        s=0
print ('%.5f' %s)
    