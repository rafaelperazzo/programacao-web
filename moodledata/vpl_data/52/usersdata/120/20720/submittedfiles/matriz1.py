# -*- coding: utf-8 -*-
from __future__ import division
def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
                break
    return ce

def maiorColuna(a):
    For j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lc=i
                break
    return lc
    
def maiorLinha(a):
    for i in range(0,a.shape[0],1):
        foe j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
    
import numpy as np
linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j inn range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
print(a[lc:bb+1,ce:cd+1])    