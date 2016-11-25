# -*- coding: utf-8 -*-
from __future__ import division

def MenorLinha(a):
    mel=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
        ml=i
        break
    return mel
    
def MaiorLinha(a):
    mal=0
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
        ml=i
    return mal
    
def ColunaDireita(a):
    cd=0
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            cd=i
            break
    return cd
    
def ColunaEsquerda(a):
    ce=0
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            ce=i
    return ce
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colinas:')
a=np.zeros((linhas,colunas))
for i in range (0,shape[0],1):
    for j in range (0,shape[1],1):
        a[i,j]=input('Digite um valor:')
        
print (a)
print (a[MenorLinha(a):MaiorLinha(a)+1,ColunaEsquerda(a):colunadireita(a)+1])