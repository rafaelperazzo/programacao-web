# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Digite a dimensão da matriz:')
a=np.zeros((n,n))

i1=input('digite o indice da linha:')
i2=input('digite o indice da coluna:')

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento')
        
def somalinha(a):
    cont=0
    for j in range(0,a.shape[1],1):
        cont=cont+a[i1-1,j]
    cont=cont-a[i1-1,i2-1]
    return cont
    
def somacoluna(a):
    cont=0
    for i in range(0,a.shape[0],1):
        cont=cont+a[i,i2-1]
    cont=cont-a[i1-1,i2-1]
    return cont
    
b=somalinha(a)+somacoluna(a)
print b