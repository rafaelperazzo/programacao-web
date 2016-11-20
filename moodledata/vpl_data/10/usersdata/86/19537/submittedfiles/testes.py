# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE AQUI ABAIXO
def mdm(x):
    
    direita=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j>=direita:
                    direita=j
    esquerda=x.shape[0]-1
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j<=esquerda:
                    esquerda=j
    baixo=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i>=baixo:
                    baixo=i
    cima=x.shape[1]-1
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i<=cima:
                    cima=i
    linhas=direita-esquerda
    colunas=baixo-cima
    b=np.zeros((linhas,colunas))
    for i in range(0,linhas,1):
        for j in range(0,colunas,1):
            x[i,j]=b[esquerda+j,cima+i]
    return b
linhas= input('l:')
colunas=input('c:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=input('digite:')
            
print mdm(a)
    
   
