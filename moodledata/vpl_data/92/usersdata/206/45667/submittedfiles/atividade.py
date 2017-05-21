# -*- coding: utf-8 -*-
import math

n=int(input('Digite n:'))
if (n<0):
    n=n*(-1)
i=1
s=0

for i in range(1,n+1,1):
    d=i/n
    s=s+d
    n=n-1
print('%.5f' %s)
   