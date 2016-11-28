# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagonal_principal(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return somadp
    
def soma_diagonal_secundaria(b):
    soma=0
    for i in range(0,b.shape[0],1):
        soma=soma+b[i,b.shape[0]-i-1]:
    return somads
    
def soma_linha(c):
    c=[]
    for i in range (0,c.shape[0],1):
        soma=0
        for j in range (0,c.shape[1],1):
            soma=soma+a[i,j]
        a.append(soma)
        
    return somal
    
def soma_coluna(d):
    d=[]
    for j in range(0,d.shape[1],1):
        soma=0
        for i in range(0,d.shape[0],1):
            soma=soma+a[i,j]
        a.append(soma)
    return somac
    
def magico(a):
    if somadp==somads==somal==somac:
        return s
        
    else:
        return N
        
linhas=input('digite a quantidade de linhas')
colunas=input('digite a quantidade de colunas')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento:')

m=magico(a)        
print m
        
