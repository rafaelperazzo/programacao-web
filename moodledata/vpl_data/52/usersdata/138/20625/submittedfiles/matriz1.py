# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunaEsquerda(a):
    ce=0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
                break
    return ce
    
def colunaDireita(a):
    cd=0
    i=0
    j=a.shape[1]-1
    while j>=0:
        while i<=a.shape[0]-1:
            if a[i,j]==1:
                cd=j
                break
            i=i+1
        j=j-1
    return cd
def linhaCima(a):
    lc=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lc=i
                break
    return lc

def linhaBaixo(a):
    lb=0
    i=a.shape[0]-1
    j=a.shape[1]-1
    while i<=a.shape[0]-1 and i>=0:
        while j<=a.shape[1]-1 and j>=0:
            if a[i,j]==1:
                ib=i
                break
            j=j-1
        i=i-1
    return lb
linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')

linhaCima(a)=lc
linhaBaixo(a)=lb
print (a[lc:lb+1,:])
    
    
    
    
    
    
    
    
    
    
    