# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Valor de n: ')
if n<0:
    n=n*(-1)
x=0
s=0

for i in range (1,n+1,1):
        x=i/n
        n=n-1
        s=s+x
print ('%.5f')%s
