# -*- coding: utf-8 -*-
from __future__ import division
def degrau(x):
    d=[]
    for i in range (0,len(x)-1,1):
        y=x[i+1]-x[i]
        if (y<0):
            y=(-1)*y
        d.append(x)
    return d
def degraumaior(m):
    x=m[0]
    for i in range (1,len(m),1):
        if (a<m[i]):
            a=m[i]
    return a
n=input('quantidade de termos da lista:')
x=[]
for i in range(0,n,1):
    x.append(input('digite o elemento:'))
y=degrau(x)
z=degraumaior(y)
print (z)
        