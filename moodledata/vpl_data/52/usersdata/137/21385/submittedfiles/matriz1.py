# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def colunaEsquerda (a):
    ce=0
    for j in range (0,a.shape[1],1):
        if 1 in a [:,1:(i+1)]:
            ce=i
            break
    return ce
def colunaDireita (a):
    cd=0
    for j in range (0,a.shape[1],1):
        if 1 in a [:,i:(i+1)]:
            cd=i
    return cd
def linhaCima (a):
    lc=0
    for i in range (0,a.shape[0],1):
        if 1 in a [1:(i+1),:]:
            lc=i
            break
    return lc
def linhaBaixo (a):
    lb=0
    for i in range (0,a.shape[0],1):
        if 1 in a [i:(i+1),:]:
            lb=i
    return lb

linhas =input('linhas:')
colunas=input('colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))
ce=colunaEsquerda(a)
cd=colunaDireita(a)
lc=linhaCima(a)
lb=linhaBaixo(a)
print (a[lc:lb+1,ce:cd+1])
