# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas=input('numero de linhas:')
colunas=input('numero de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elementos:')
        
def colunaEsquerda(a):
    ce=0
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            ce=i
            break
    return ce
    
def colunaDireita(a):
    cd=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            cd=i
    return cd
    
def primeira_linha(a):
    pL=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            pL=i
            break
    return pL
    
def ultima_linha(a):
    iL=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            uL=i
    return uL
    
print a[primeira_linha(a):(ultima_linha(a)+1),colunaEsquerda(a):(colunaDireita(a)+1)]
