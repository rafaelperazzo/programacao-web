# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def peso(d,a,b):
    s=0
    e=0
    for j in range(0,d.shape[0],1):
        if(j!=b):
            s=s+d[a,j]
    for i in range(0,d.shape[0],1):
        if(i!=a):
            e=e+d[i,b]
    p=s+e
    return p

n=input('Digite a dimensão da matriz:')
f=input('Digite o índice da linha para a descoberta do peso:')
g=input('Digite o índice da coluna para a descoberta do peso:')
d=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        d[i,j]=input('Digite o valor do elemento:')
print ('O peso é:%d' %peso(d,f,g))
