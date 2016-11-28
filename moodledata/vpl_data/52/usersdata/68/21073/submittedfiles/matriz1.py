# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def menorColuna(a):
    for j in range (0, a.shape[1],1):
        for i in range (0, a.shape[0],1):
            if a[i,j]==1:
                ce=j
                return ce
    
def maiorColuna(b):
    for j in range (0, b.shape[1],1):
        for i in range (0, b.shape[0],1):
            if b[i,j]==1:
                cd=j
    return cd

def menorLinha(c):
    for i in range (0, c.shape[0],1):
        for j in range (0, c.shape[1],1):
            if c[i,j]==1:
                return lc

def maiorLinha(d):
    for i in range (0, d.shape[0],1):
        for j in range (0, d.shape[1],1):
            if d[i,j]==1:
                lb=i
    return lb

#PROGRAMA PRINCIPAL
linhas= input('Digite a quantidade de linhas:')
colunas= input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range (0, a.shape[0],1):
    for j in range (0, a.shape[1],1):
        a[i,j]= input ('Digite um elemento da matriz a:')

ce=menorColuna(a)
cd=maiorColuna(a)
lc=menorLinha(a)
lb=maiorLinha(a)

print (a[lc:lb+1,ce:cd+1])