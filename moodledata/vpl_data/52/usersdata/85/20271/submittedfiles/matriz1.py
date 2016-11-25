# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def linha1(a):
    for i in range(0,a.shape[0],1):
        if 1 in a[i:i+1, :]:
            b=i
            break
    return b

def linha2(a):
    bm=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i:i+1, :]:
            b=i
            if b>bm:
                bm=b
    return bm

def coluna1(a):
    for i in range(0,a.shape[1],1):
        if 1 in a[:, i:i+1]:
            b=i
            break
    return b
    
def coluna2(a):
    bm=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:, i:i+1]:
            b=i
            if b>bm:
                bm=b
    return bm
    
l= input('Digite o número de linhas: ')
c= input('Digite o número de colunas: ')
a= np.zeros((l,c))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]= input('Digite o elemento da matriz: ')
        
l1= linha1(a)
l2= linha2(a)
c1= coluna1(a)
c2= coluna2(a)

print a
print a[l1:(l2+1), c1:(c2+1)]