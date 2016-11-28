# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def diagonalP(a):
    soma=0
    for i in range (0, a.shape[0],1):
        soma=soma+a[i,i]
    return soma

def diagonalS(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while j>=0:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma

def soma_linhas(a):
    l=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append (soma)
    return l

def soma_colunas(a):
    c=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        c.append (soma)
    return c

def quadrado_magico(a):
    sdp=diagonalP(a)
    sds=diagonalS(a)
    sl=soma_linhas(a)
    sc=soma_colunas(a)
    cont=0
    for i in range (0,len(sl),1):
        if sdp==sds==sl[i]==sc[i]:
            cont=cont+1
    if cont==len(sl):
        return True
    else:
        return False 
        
n=input('digite a dimensão:')
a=np.zeros ((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('digite um elemento da matriz:')
        
if quadrado_magico(a):
    print ('S')
else:
    print ('N')
