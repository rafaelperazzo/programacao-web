# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def mdm(x):
    direita=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j>direita:
                    direita=j
    esquerda=x.shape[1]-1
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j<esquerda:
                    esquerda=j
    cima=x.shape[0]-1
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i<cima:
                    cima=i
    baixo=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i>baixo:
                    baixo=i

    colunas= direita-esquerda
    linhas= baixo-cima
    b=np.zeros((linhas,colunas))
    for i in range(0,linhas+1,1):
        for j in range(0,colunas+1,1):
            b[i,j]=x[esquerda+j,cima+i]
    return b
                
linhas= input('linhas:')
colunas= input('colunas:')
a= np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite valor a:')
print (mdm(a))

