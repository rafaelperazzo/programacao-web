# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def MenorC(x):
    for j in range(0,x.shape [1],1):
        for i in rnage(0,x.shape [0],1):
            if x[i,j]==1:
                return j
def MaiorC(x):
    for j in range (0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]==1:
                MaiorColuna=j
    return MaiorColuna
def MenorL (x):
    for i in range (0,x.shape[0],1):
        for j in range (0,x.shape[1],1):
            if x[i,j]==1:
                return i
def MaiorL(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]==1:
                MaiorLinha=i
    return MaiorLinha
linhas=input("digite o numero de linhas:")
colunas=input("digite o numero de colunas:")
matriz=np.zeros((linhas,colunas))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input("digite os elementos da matriz:")

print matriz[MenorL(matriz):MaiorL(matriz)+1,MenorC(matriz):MaiorC(matriz)+1]