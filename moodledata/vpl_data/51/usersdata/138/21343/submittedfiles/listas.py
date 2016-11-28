# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    d=[]
    for i in range(0,len(a)-1,1):
        b=a[i+1]-a[i]
        if (b < 0):
            b=(-1)*b
        d.append(b)
    return d

def maiordegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            maior=a[i]
            if maior<a[i]:
                maior=a[i]
    return maior
    

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
c=degrau(a)
m=maiordegrau(a)
print m

