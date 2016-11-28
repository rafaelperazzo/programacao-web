# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    a=[]
    for i in range(0,len(a)-1,1):
        b=a[i+1]-a[i]
        if (b < 0):
            b=(-1)*b
        a.append(b)
    return a

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
c=degrau(a)
print c

