# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n = input("dimensão:")
a = np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elementos:')

def somaDP(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma =soma+matriz[i,i]
    return soma

def somaDS(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma =soma+matriz[i,(matriz.shape[0]-i-1)]
    return soma
    
def somaL(matriz):
    soma=[]
    for i in range(0,matriz.shape[0],1):
        soma.append(sum(matriz[i,:]))
    return soma

def somaC(matriz):
    soma = []
    for i in range(0,matriz.shape[0],1):
        soma.append(sum(matriz[:,1]))
    return soma
    
def qmagico(matriz):
    sd1 = somaDP(matriz)
    sd2 = somaDS(matriz)
    sL = somaL(matriz)
    sC = somaC(matriz)
    cont = 0 
    for i in range(0,len(sL),1):
        if sd1==sd2==sL[i]==sC[i]:
            cont = cont+1
    if cont==len(sL):
        return True
    else:
        return False
    
if qmagico(a):
    print 'S'
else:
    print 'N'
    