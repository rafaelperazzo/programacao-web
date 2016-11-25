# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_coluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j

def maior_coluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                CD=j
    return CD

def menor_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i

def maior_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                LB=i
    return LB
    
linhas=input('Digite a quantidade de linhas da matriz:')
colunas=input('Digite a quantidade de colunas da matriz:')
m=np.zeros((linhas,colunas))

for i in range(0,m.shape[0],1):
    for j in range(0,m.shape[1],1):
        m[i,j]=input('Digite um elemento:')
        
CE=menor_coluna(m)
CD=maior_coluna(m)
LC=maior_linha(m)
LB=menor_linha(m)
print m
print (m[CE:CD+1,LC:LB+1])
