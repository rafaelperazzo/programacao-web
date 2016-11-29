# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j
                
def colunaDireita(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def linhaCima(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def linhaBaixo(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
def recorteRetangular(a):
    ce=colunaEsquerda(a)
    cd=colunaDireita(a)
    
    lc=linhaCima(a)
    lb=linhaBaixo(a)
    return a[lc:lb+1,ce:cd+1]

n=input('digite a quantidade de linhas:')
m=input('digite a quantidade de colunas:')
a=np.zeros((n,m))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite os elementos da matriz:')
        
print recorteRetangular(a)
