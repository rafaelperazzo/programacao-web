# -*- coding: utf-8 -*-
from __future__ import division

def colunaEsquerda(a):
    a=np.zeros((linhas,colunas))
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce=i
            break
    return ce

def colunaDireita(a):
    a=np.zeros((linhas,colunas))
    cd=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            cd=i
    return cd

def linhaCima(a):
    a=np.zeros((linhas,colunas))
    lc=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            lc=i
            break
    return lc

def linhaBaixo(a):
    a=np.zeros((linhas,colunas))
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

