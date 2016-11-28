# -*- coding: utf-8 -*-
from __future__ import division

def mod(x,y):
    b=x-y
    if b>=0:
        return b
    else:
        return b*(-1)
def degrau(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        deg=mod(lista[i],lista[i+1])
        if deg>=maior:
            maior=deg
    return maior
    
n=input('n:')
a=[]
for i in range(0,n,1):
    a.append(input('a:'))
print degrau(a)