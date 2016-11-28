# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_linha(o):
    for i in range (0,a.shape[0],1):
        for j in range (0,shape[1],1):
            if a[i,j]==1:
                return i
            
def menor_coluna(o):
    for j in range(0,a.shape[1],1):
        for i in range(0,shape[0],1):
            if a[i,j]==1:
                return j
                
                

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a qunatidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento')
        
print menor_linha(a)

        