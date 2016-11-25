# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    
    d=0
    for i in range(0, len(a)-1, 1):
        if a[i]<0:
            a[i]= a[i]*(-1)
        if a[i+1]<0:
            a[i+1]= a[i+1]*(-1)
        x= a[i]-a[i+1]
        if x<0:
            x=x*(-1)
        if x>d:
            d=x
    return d

n= int(input('Digite n: '))
a=[]
for i in range(0, n, 1):
    a.append(input('Digite um valor a: '))

print degrau(a)


