# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#ENCONTRAR COLUNA DA ESQUERDA
def menor_coluna(a):
    for j in range(0, a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                return j
    
#ENCONTRAR COÇUNA DA DIREITA
def maoior_coluna(a):
    for j in range (0,a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
#ENCONTRAR LINHA DE CIMA
def menor_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
            
#ENCONTRAR LINHA DE BAIXO
def maior_linha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
    
linhas=input('digite o numero de linhas:')
colunas=input('digite o numero de colunas:')
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=input('digite um elemento:')
    

print (a[menor_linha(a):maior_linha(a)+1,menor_coluna(a):maior_coluna(a)+1])



