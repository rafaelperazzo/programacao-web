# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def linha1(a):
    for i in range(0, a.shape[0],1):
        if 1 in a[i:i+1, :]:
            b = i
            break
    return b
    
    
def linha2(a):
    b=0
    for i in range(0, a.shape[0], 1):
        if 1 in a[i:i+1, :]:
            b1 = i
            if b1>b:
                b=b1
    return b
    
    
def coluna1(a):
    for j in range(0, a.shape[1],1):
        if 1 in a[:, i:i+1]:
            b=1
            break
    return b
    
    
def coluna2(a):
    b=0
    for i in range(0, a.shape[1], 1):
        if 1 in a[:,i:i+1]:
            b1=i
            if b1>b:
                b=b1
    return b
    
    
n=input('digite o numero de linhas da matriz:')
m=input('digite o numero de colunas da matriz:')
a= np.zeros((n,m))
for i in range(0,n,1):
    for j in range(0,m,1):
        a[i,j]= input('digite o elemento da matriz:')
b = linha1(a)
c = linha2(a)
d = coluna1(a)
f = coluna2(a)

print a[b:(c+1), d:(f+1)]
