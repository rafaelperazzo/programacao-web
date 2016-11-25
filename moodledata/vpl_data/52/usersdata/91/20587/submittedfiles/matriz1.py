# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import shape 
def menorcoluna(a):
    ce=0
    for j in range(0,a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                ce=j
                return ce

def maiorcoluna(a):
    cd=0
    for j in range(0,a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha(a):
    lc=0
    for i in range(0,a.shape[0],1):
        for j in range(0, a.shape[1],1):
            if a[i,j]==1:
                lc=i
                return lc
    
def maiorlinha(a):
    lb=0
    for i in range(0,a.shape[0],1):
        for j in range(0, a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb

a=[]    
m=input('digite o numero de colunas:')
n=input('digite o numero de linhas:')
for i in range(0,n,1):
    for j in range(0,m,1):
        a.append(input('digite o elemento:'))
        
esquerdo=menorcoluna(a)
direito=maiorcoluna(a)
cima=menorlinha(a)
baixo=maiorlinha(a)

print (a[cima:baixo+1, esquerdo:direito+1])
