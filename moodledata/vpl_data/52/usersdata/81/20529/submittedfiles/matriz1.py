# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def cesquerda(a):
    colunae=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                colunae=j
                return colunae
    
def cdireita(a):
    colunad=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while j>=0:
        while i>=0:
            if a[i,j]==1:
                colunad=j
                break
            i=i-1
        j=j-1
    return colunad
    
    
def lcima(a):
    linhac=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                linhac=i
                break
    return linhac
    
def lbaixo(a):
    linhab=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while i>=0:
        while j>=0:
            if a[i,j]==1:
                linhab==i
            j=j-1
        i=i-1
    return linhab
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor da matriz a:')
    
cima= lcima(a)
baixo= lbaixo(a)
esquerda= cesquerda(a)
direita= cdireita(a)

print a[cima:baixo+1,esquerda:direita+1]