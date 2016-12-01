# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinha(a,n):
    soma=0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            soma=soma+a[n,j]
    return soma

def somacoluna(a,n):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,n]
    return soma

def somatotal (a,n,x,y):
    soma=0
    soma=somalinha(a,n)+somacoluna(n,a)-(2*a[x,y])
    return soma

#PROGRAMA PRINCIPAL 
n=input('Digite a dimensão da matriz:')
a=np.zeros ((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('Digite um elemento da matriz a:')
x=input ('Digite a coordenada da linha:')
y=input ('Digite a coordenada da coluna:')

soma_total=somatotal(a,n,x,y)
print soma_total 