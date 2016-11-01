# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('n:')
l=[]
for i in range (0,n,1):
    l.append(input('Dgigite uma nota:'))
s=0
for i in range (0,n,1):
    s=s+l[i]
m=s/n
x=0
for i in range (0,n,1):
    x=x+((l[i]-m)**2)
dp=((x/(n-1))**0.5)
print ('%.22f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %m)
print ('%.2f' %dp)