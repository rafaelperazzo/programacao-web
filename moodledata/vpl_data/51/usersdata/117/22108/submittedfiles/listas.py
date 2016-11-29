# -*- coding: utf-8 -*-
from __future__ import division


def md(a):
    m=0
    for i in range (0,len(a)-1,1):
        de=abs(a[i]-(a[i+1]))
        if de>m:
            m=de
    return m
    
n=input('Digite a quantidade de elementos')

a=[]

for i in range (0,n,1):
    a.append(input('Digite a lista: '))
    
print md(a)
    