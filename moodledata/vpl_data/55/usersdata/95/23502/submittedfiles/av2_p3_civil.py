# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_coluna(a,y):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
    return soma

def soma_linha(a,x):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[x,j]
    return soma

n=input('Dimensão da matriz:')
x=input('Indice da linha:')
y=input('Indice da coluna:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Elementos da matriz:')
    
b=soma_coluna(a,y)
d=soma_linha(a,x)

r=b+c-(2*a[x,y])

print r
