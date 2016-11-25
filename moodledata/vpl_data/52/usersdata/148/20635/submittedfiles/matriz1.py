# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import numpy np

def colunaEsquerda(a):
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce=i
            break
    return ce

def colunaDireita(a):
    cd=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            cd=i
    return cd

def linhaCima(a):
    lc=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            lc=i
            break
    return lc

def linhaBaixo(a):
    lb=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            lb=i
    return lb
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')


print(a[linhaCima(a):linhaBaixo(a)+1,colunaEsquerda(a):colunaDireita(a)+1])

