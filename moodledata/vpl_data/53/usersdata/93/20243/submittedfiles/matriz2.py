# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
def diag1(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,i]
    return s
def diag2(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,a.shape[1]-1-i]
    return s
def linha(a,n):
    s=0
    for i in range(0,a.shape[1],1):
        s=s+a[n,i]
    return s
def coluna(a,n):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,n]
    return s
def quadradoMagico(a):
    b=[]
    b.append(diag1(a))
    b.append(diag2(a))
    for i in range(0,a.shape[0],1):
        b.append(linha(a,i))
        b.append(coluna(a,i))
    cont=0
    for i in range(1,len(b),1):
        if b[0]!=b[i]:
            cont=cont+1
    if cont==0:
        return 'S'
    else:
        return 'N'

n=input('dimensão: ')
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('elemento de a: ')
print quadradoMagico(a)
