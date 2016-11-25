# -*- coding: utf-8 -*-
from __future__ import division
def mdegrau(x):
    degrau=0
    for i in range(0,len(x)-1,1):
        s=x[i+1]-x[i]
        if s<0:
            s=s*(-1)
        if s>degrau:
            degrau=s
    return degrau
n=int(input('Digite a quantidade de números da lista:'))
a=[]
for i in range(0,n,1):
    a.append(input('Digite um número:'))
print mdegrau(a)
