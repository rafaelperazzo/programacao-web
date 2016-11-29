# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def menorcoluna(lista):
    for j in range(0,lista.shape[1],1):
        if lista[i,j]==1:
            return j
def maiorcoluna(lista):
    for j in range(0,lista.shape[1],1):
        if lista[i,j]==1:
            md=j
    return md
def menorlinha(lista):
    for i in range(0,lista.shape[0],1):
        if lista[i,j]==1:
            return i 
def maiorlinha(lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if lista[i,j]==1:
                ld=i
    return ld
linhas=input('digite o numero de linhas:')
colunas=input('digite o numero de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):]
        a[i,j]=input('insira um elemento:')
print (a[menorlinha (a):maiorlinha (a)+1,menorcoluna(a):maiorcoluna(a)+1)

