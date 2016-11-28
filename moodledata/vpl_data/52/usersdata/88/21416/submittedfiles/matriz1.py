# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_coluna(a):
    for j in range (0, a.shape[1],1):
        for i in range (0, a.shape[0],1):
            if a[i,j]==1:
                return j

def maior_coluna(a):
    for j in range (0, a.shape[1],1):
        for i in range (0, a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd

def menor_linha(a):
    for i in range (0, a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if a[i,j]==1:
                return i

def maior_linha(a):
    for i in range (0, a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('Digite um elemento da matriz:')
        
col_esq=menor_coluna(a)
col_dir=maior_coluna(a)
lin_cima=menor_linha(a)
lin_bai=maior_linha(a)

print (a[lin_cima:lin_bai+1,col_esq:col_dir+1])
