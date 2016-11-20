# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

import numpy as np

def soma(a,b):
    
    for i in range (0,soma.shape[0],1):
        for j in range (0,soma.shape[1],1):
            soma[i,j]=a[i,j]+b[i,j]
        
    return soma

linhas=input('Quantidade de linhas: ')
colunas=input('Quantidade de colunas: ')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um termo de A: ')

b=np.zeros((linhas,colunas))

for i in range (0,b.shape[0],1):
    for j in range (0,b.shape[1],1):
        b[i,j]=input('Digite um termo de B: ')
        
soma=np.zeros((linhas,colunas))

print soma(a,b)