# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha(a,linha):
    somaL=0
    for j in range (0,a.shape[1],1):
        somaL=somaL+a[linha,j]
        
    return somaL
    
def somaColuna(a,coluna):
    soma=0
    for i in range (0,a.shape[0],1):
        somaC=somaC+a[i,coluna]
        
    return somaC
    
def peso(a,linha,coluna):
    somaTotal=somaC(a,coluna)+somaL(a,linha)-(2*a[linha,coluna])
    
n=input('Digite o valor da dimensão da matriz:')
m=input('Digie o valor da posição de m:')
n=input('Digite o valor da posição de n:')

a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o valor de cada elemento da matriz:')
        
print peso(a,m,n)
