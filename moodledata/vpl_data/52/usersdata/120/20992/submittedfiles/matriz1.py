# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def menorColuna(lista):
    for j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if a[i,j]==1:
                return j

def maiorColuna(lista):
    For j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorLinha(lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if a[i,j]==1:
                return i
    
def maiorLinha(lista):
    for i in range(0,lista.shape[0],1):
        foe j in range(0,lista.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb
    
    
linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
        
print(a[menorLinha(a):maiorLinha(a)+1,menorColuna(a):maiorColuna(a)+1])    