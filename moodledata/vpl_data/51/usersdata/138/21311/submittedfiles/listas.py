# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    a=[]
    cont=0
    for i in range(0,len(lista)-1,1):
        if a[i]>=a[i+1]:
            cont=a[i]-a[i+1]
        else:
            cont=a[i+1]-a[i]
    return a

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
c=degrau(lista)
print c

