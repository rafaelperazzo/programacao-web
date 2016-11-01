# -*- coding: utf-8 -*-
from __future__ import division
n=input('n:')
l=[]
for i in range (0,n,1):
    l.append(input('Digite uma nota:')
s=0
for i in range (0,n,1):
    s=s+l[i]
m=s/n
h=0
for i in range (0,n,1):
    h=h+((l[i]-med)**2)
dp=((h/(n-1))**0.5)
print ('%.2f' %l[0]
print ('%2f' %l[n-1])
print ('%.2f' %m)
print ('%.2f' %dp)
    