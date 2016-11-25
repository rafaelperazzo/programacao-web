# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def cesquerda(a):
    colunae=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                colunae=j
                break
    return colunae
    
def cdireita(a):
    coluna=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while j>=0:
        while i>=0:
            if a[i,j]==1:
                coluna=j
                break
            i=i-1
        j=j-1
    return coluna
    
def lcima(a):
    linha=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                linha=i
                break
    return linha
    
def lbaixo(a):
    linha=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while i>=0:
        while j>=0:
            if a[i,j]==1:
                linha==i
                break
            j=j-1
        i=i-1
    return linha
    
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