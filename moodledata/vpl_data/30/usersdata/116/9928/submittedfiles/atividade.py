# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('insira n:'))
if n<0:
    n=-n
i=1
s=0

while n>=1: 
    s=(i/n)+s
    n=n-1
    i=i+1
    
print ('%.5f' %s)
    