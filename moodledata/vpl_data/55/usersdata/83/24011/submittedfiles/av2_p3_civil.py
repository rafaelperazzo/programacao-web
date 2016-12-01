# -*- coding: utf-8 -*-
from __future__ import division

def peso(X,a,b):
    c=0
    d=0
    for i in range (0,X.shape[0],1):
        if(i!=a):
            d=d+X[i,b]
    for j in range (0,X.shape[0],1):
        if(i!=b):
            c=c+X[a,j]
    e=c+d
    return e

n=input('Digite a dimensão da matriz:   ')
linha=input('Digite a linha que quer saber o peso:   ')
coluna=input('Digite a coluna que quer saber o peso:   ')

X=np.zeros((n,n))

for i in range (0,n,1):
    for j in range (0,n,1):
        X[i,j]=input('Digite o valor do elemento:   ')

print ('O peso na linha %d e na coluna %d é: %d' %linha,coluna,peso(X,linha,coluna))
