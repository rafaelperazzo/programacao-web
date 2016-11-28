# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#FUNÇÕES
def MenorC(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]==1:
                return j
    
def MaiorC(X):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]==1:
                MaiorColuna=j
    
    return MaiorColuna

def MenorL(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                return i
def MaiorL(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                MaiorLinha=i
    
    return MaiorLinha

#PRINCIPAL
linhas=input('Digite o número de linhas: ')
colunas=input('Digite o número de colunas: ')

matriz=np.zeros((linhas,colunas))

for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            matriz[i,j]=input('Digite os elementos da matriz: ')

print(matriz[MenorL(matriz):MaiorL(matriz)+1,MenorC(matriz):MaiorC(matriz)+1])
            
