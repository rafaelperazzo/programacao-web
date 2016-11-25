# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def mdm(x):
    
    cmax=0
    for i in range(0, x.shape[0], 1):
        for j in range(0, x.shape[1], 1):
            if x[i,j]==1:
                if j>cmax:
                    cmax=j
    
    cmin=x.shape[1]-1
    for i in range(0, x.shape[0], 1):
        for j in range(0, x.shape[1], 1):
            if x[i,j]==1:
                if j<cmin:
                    cmin=j
    
    lmax= 0
    for i in range(0, x.shape[0], 1):
        for j in range(0, x.shape[1], 1):
            if x[i,j]==1:
                if i>lmax:
                    lmax=i
    
    lmin= x.shape[0]-1
    for i in range(0, x.shape[0], 1):
        for j in range(0, x.shape[1], 1):
            if x[i,j]==1:
                if i<lmin:
                    lmin=i
    
    linhas= lmax-lmin+1
    colunas= cmax-cmin+1
    a=np.zeros((linhas,colunas))
    for i in range(0, linhas, 1):
        for i in range(0, colunas, 1):
            a[i,j]= x[lmin+i, cmin+j]
    return a

linhas= input('Digite o numero de linhas: ')
colunas= input('Digite o numero de colunas: ')

a=np.zeros((linhas, colunas))
for i in range(0, linhas, 1):
    for i in range(0, colunas, 1):
        a[i,j]= input('Digite um valor de a: ')

print mdm(a)
    