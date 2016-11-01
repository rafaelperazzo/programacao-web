# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite uma quantidade:')
a=[]

for i in range(0,n,1):
    a.append(input('digite um elemento:'))

j=0
b=0

for i in range(0,n,1):
    b=a[j]+b
    j=j+1

c=a[0]
h=a[n-1]
k=b/n

print(c)
print(h)
print(k)
     
