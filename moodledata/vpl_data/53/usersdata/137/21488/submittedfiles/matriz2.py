# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha(a):
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    return b

def somaColunas(a):
    b=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        b.append(soma)
    return b

def somaDiagonalP(a):
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,i]
    return soma

def somaDiagonalS(a):
    soma=0
    for i in range (0,a.shape[0],1):
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,i]
    return soma

def quadradomagico(a):
    sl=somaLinha(a)
    sc=somaColunas(a)
    dp=somaDiagonalP(a)
    ds=somaDiagonalS(a)
    cont=0
    for i in range (0,len(sl),1):
        if dp==ds==sc[i]==sl[i]:
            cont=cont+1
    if cont==len(sl):
        return True
    else:
        return False
n=input('n:')
a=np.zeros((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]=input('digite um valor:')
if quadradomagico(a):
    print('S')
else:
    print ('N')
    
