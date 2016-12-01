# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinha(a,x):
    soma=0
    for j in range(0,a.shape[1],1):
        soma+=a[x,j]
    return soma
    
def somacoluna(a,y):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,y]
    return soma
    
def peso(a,x,y):
    soma=0
    soma=somacoluna(a,y)+somalinha(a,x)-2*a[x,y]
    return soma

n=input('Digite a dimensão da matriz:')
x=input('Digite o indice da linha:')
y=input('Digite o indice da coluna:')

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz:')
    
    
print peso(a,x,y)