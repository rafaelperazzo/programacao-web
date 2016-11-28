# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    a=[]
    for i in range(0,len(a)-1,1):
        if a[i]>=a[i+1]:
            cont=a[i]-a[i+1]
        else:
            cont=a[i+1]-a[i]
        a.insert(0,cont)
    return cont

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
c=degrau(a)
print c

