# -*- coding: utf-8 -*-
from __future__ import division

def mdm(x):
    direita=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j>=direita:
                    direita=j
    esquerda=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if j<=esquerda:
                    esquerda=j
    cima=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i<=cima:
                    cima=i
    baixo=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                if i>=baixo:
                    baixo=i

    colunas= direita-esquerda
    linhas= baixo-cima
    b=np.zeros((linhas,colunas))
    for i in range(0,colunas,1):
        for j in range(0,linhas,1):
            b[i,j]=x[esquerda+j,cima+i]
    return b
                
