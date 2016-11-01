# -*- coding: utf-8 -*-
from __future__ import division
n=input('n:')
l=[]
for i in range (0,n,1):
    l.append(input('Digite uma nota:'))
s=0
for i in range (0,n,1):
    s=s+l[i]
m=s/n
print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %m)
print (l)
    