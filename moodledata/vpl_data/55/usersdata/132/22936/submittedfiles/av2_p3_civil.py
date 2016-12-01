# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def pesol(a,x,y):
    s1=0
    for i in range(0,x,1):
        for j in range(0,a.shape[1],1):
            s1=s1+a[i,j]
    return s1        
            


n=input('digite as dimensoes da matriz:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o valor:')
x=input('digite o indice da linha:')
y=input('digite o indica da coluna:')
print(pesol(a,x,y)