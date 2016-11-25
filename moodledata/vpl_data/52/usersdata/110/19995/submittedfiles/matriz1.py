# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def menorLinha(a):
    ml=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            ml=i
            break
    return ml
      
def maiorLinha(a):
    mal=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            mal=i
    return mal
def colunaesquerda(a):
    ce=0
    for j in range(0,a.shape[1],1):
        if 1 in a[:,j]:
            ce=j
            break
    return ce
def colunadireita(a):
    cd=0
    for j in range(0,a.shape[1],1):
        if 1 in a[:,j]:
            cd=j
    return cd
linhas=input('Digite a quant. de linhas: ')
colunas=input('Digite quant. de colunas: ')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor: ')
print(a[menorLinha(a):maiorLinha(a)+1,colunaesquerda(a):colunadireita+1])