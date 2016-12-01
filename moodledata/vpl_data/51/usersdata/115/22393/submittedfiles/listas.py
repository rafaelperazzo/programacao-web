# -*- coding: utf-8 -*-
from __future__ import division
def degrau(a):
    d=[]
    for i in range (0,len(a)-1,1):
        b=a[i+1]-a[i]
        if (b<0):
            b=(-1)*b
        d.append(b)
    return d
def degraumaior(s):
    a=s[0]
    for i in range (1,len(s),1):
        if (a<s[i]):
            a=s[i]
    return a
n=input('quantidade de termos da lista:')
a=[]
for i in range(0,n,1):
    a.append(input('digite o elemento:'))
b=degrau(a)
c=degraumaior(b)
print (c)
        