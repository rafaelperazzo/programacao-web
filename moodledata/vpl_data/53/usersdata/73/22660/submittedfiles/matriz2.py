# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('insira a dimensao da matriz:')
a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('um valor:')

def soma_diagonalP (matriz):
    soma=0
    for i in range (0,matriz.shape[0],1):
        soma=soma+matriz[i,i]
    return soma
    
def soma_diagonalS (matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,(matriz.shape[0]-i-1)]
    return soma
    
def soma_linhas (matriz):
    soma=[]
    for i in range (0,matriz.shape[0],1):
        soma.append(sum(matriz[i,:]))
    return soma
    
def soma_coluna (matriz):
    soma=[]
    for i in range (0,matriz.shape[0],1):
        soma.append(sum(matriz[:,i]))
    return soma
    
def qmagico (matriz):
    sd1=soma_diagonalP (matriz)
    sd2=soma_diagonalS (matriz)
    sL=soma_linhas (matriz)
    sC=soma_coluna (matriz)
    cont=0
    for i in range (0,len(sL),1):
        if sd1==sd2==sL[i]==sC[i]:
            cont=cont+1
    if cont==len(sL):
        return True
    else:
        return False

if qmagico (a):
    print ('S')
else:
    print ('N')
