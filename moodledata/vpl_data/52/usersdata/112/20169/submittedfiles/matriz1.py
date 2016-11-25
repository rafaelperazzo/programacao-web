# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o elemento:')
print a

def colunaE(a):
    CE=0
    for i in range(0,a.shape[0],1):
        if 1 in a[:,j]:
            CE=i
            break
    return CE
def colunaD(a):
    CD=0
    for i in range(0,a.shape[0],1):
        if 1 in a[:,j]:
            CD=i
    return CD
    
def linhaE(a):
    LE=0
    for j in range(0,a.shape[1],1):
        if 1 in a[i,:]:
            LE=i
            break
    return LE
def linhaD(LD):
    LD=0
    for j in range (0,a.shape[1],1):
        if 1 in a[i,:]:
            LD=j
    return LD
print (a[linhaE(a):linhaD(a)+1,colunaE(a):colunaD(a)+1])

