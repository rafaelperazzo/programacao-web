# -*- coding: utf-8 -*-
from __future__ import division

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
b=np.zeros((linhas,colunas))
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=input('Digite um elemento:')

print(b[linhaCima(b):linhaBaixo(b)+1,linhaEsquerda(b):linhaDireita(b)+1])

