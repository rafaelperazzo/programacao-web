# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def pesol(a,x,y):
    s1=0
    s2=0
    for i in range(x,x+1,1):
        for j in range(0,y,1):
            s1=s1+a[i,j]
    if y<(a.shape[1]-1):
        for i in range(x,x+1,1):
            for j in range(y+1,a.shape[1],1):
                s2=s2+a[i,j]
    y=s1+s2
    return y
n=input('digite as dimensoes da matriz:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o valor:')
x=input('digite o indice da linha:')
y=input('digite o indica da coluna:')
print(pesol(a,x,y))