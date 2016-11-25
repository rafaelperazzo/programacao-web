# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    b=0
    c=0
    x=0
    d=0
    for i in range(0, len(a)-1, 1):
        if a[i]<0:
            b= a[i]*(-1)
        else:
            b= a[i]
        if a[i+1]<0:
            c= a[i+1]*(-1)
        else:
            c= a[i+1]
        if a[i]<0 and a[i+1]>0:
            x= b+c
        elif a[i]>0 and a[i+1]<0:
            x= b+c
        else:
            x= b-c
        if x<0:
            x=x *(-1)
        if x>d:
            d=x
    return d

n= int(input('Digite n: '))
a=[]
for i in range(0, n, 1):
    a.append(input('Digite um valor a: '))

print degrau(a)


