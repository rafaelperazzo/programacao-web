# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaDiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma + a[i,i]

    return soma
def somaDiagonal2(a):
    soma=0
    j=a.shape[0]-1
    i=0
    while i<a.shape[0]:
        soma=soma + a[i,i]
    i=i+1
    j=j-1
    return soma

def somaLinhas(a):
    S=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma + a[i,j]
        S.append(soma)
    return S

def somaColunas(a):
    S=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma + a[i,j]
        S.append(soma)
    return S

def quadradomagico(a):
    sd1=somaDiagonal1(a)
    sd2=somaDiagonal2(a)
    
    somaL=somaLinhas(a)
    somaC=somaColunas(a)
    
    cont=0
    for i in range(0,a.shape[0],1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont=cont+1
        
    if cont==len(somaL):
        return True
    else:
        return False
    
n=input('digite n:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')
        
    if quadradomagico(a):
        print('S')
    else:
        print('N')











