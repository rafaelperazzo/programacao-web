# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def MenorLinha(a):
    mel=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            mel=i
        break
    return mel
    
def MaiorLinha(a):
    mal=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            mal=i
    return mal
    
def ColunaDireita(a):
    cd=0
    for j in range (0,a.shape[1],1):
        if 1 in a[:,j]:
            cd=j
            break
    return cd
    
def ColunaEsquerda(a):
    ce=0
    for j in range (0,a.shape[1],1):
        if 1 in a[:,j]:
            ce=j
    return ce
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colinas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')
        
print (a)
print (a[MenorLinha(a):MaiorLinha(a)+1,ColunaEsquerda(a):ColunaDireita(a)+1])