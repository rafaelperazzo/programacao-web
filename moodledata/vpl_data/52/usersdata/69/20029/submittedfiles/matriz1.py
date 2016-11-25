# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunaEsquerda(x):
    ce=0
    for i in range(0,x.shape[1],1):
        if 1 in x[:,i]:
            ce=i
            break
    return ce
def colunaDireita(x):
    cd=0
    for i in range(0,x.shape[0],1):
        if 1 in x[:,i]:
            cd=i
    return cd
def linhaCima(x):
    lc=0
    for i in range(0,x.shape[0],1):
        if 1 in x[i,:]:
            lc=i
            break
    return lc
def linhaBaixo(x):
    lb=0
    for i in range (0,x.shape[0],1):
        if 1 in x[i,:]:
            lb=i
    return lb
linha=input ('Digite a quantidade de linhas da matriz:')
coluna=input ('Digite a quantidade de colunas da matriz:')
a=np.zeros((linha,coluna))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')
m=colunaEsquerda(a)
n=colunaDireita(a)
p=linhaCima(a)
q=linhaBaixo(a)
print (a[p:q+1,m:n+1])