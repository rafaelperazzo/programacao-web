# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                return j

def maiorcoluna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
def menorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
def maiorlinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                li=j
    return li
    
linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de coluna:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o valor do elemento da matriz:')
        
print(a[menorlinha(a):maiorlinha(a)+1,menorcoluna(a):maiorcoluna(a)+1])
    