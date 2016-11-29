# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def menorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
                
def maiorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                maiorC=j
                
    return maiorC
    
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def maiorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                maiorL=i
        
    return maiorL

#CODIGO PRINCIPAL

n=input('digite o numero de linhas da matriz:')
m=input('digite o numero de colunas da matriz:')

matriz=np.zeros((n,m))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('digite os elementos da matriz :')
        
        
print(matriz[menorLinha(matriz):maiorLinha(matriz)+1,menorColuna(matriz):maiorColuna(matriz)+1])
