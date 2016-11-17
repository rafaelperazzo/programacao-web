# -*- coding: utf-8 -*-
from __future__ import division

def degrau(x,y):
    if x<0:
        x=x*(-1)
    if y<0:
        y=y*(-1)
    d= x-y
    if d<0:
        d=d*(-1)
    return d

def maior(a):
    m=0
    for i in range(0, len(a)-1, 1):
        if degrau(a[i],a[i+1])>m:
            m= degrau(a[i],a[i+1])
    return m

a=[]
n=input()
for i in range(0, n, 1):
    a.append(input())
    
print maior(a)
