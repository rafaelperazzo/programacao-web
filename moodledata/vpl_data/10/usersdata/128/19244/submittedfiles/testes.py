# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

import numpy as np

linhas=input('Quantidade de linhas: ')
colunas=input('Quantidade de colunas: ')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um termo: ')

b=np.zeros((linhas,colunas))

for i in range (0,b.shape[0],1):
    for j in range (0,b.shape[1],1):
        b[i,j]=input('Digite um termo: ')
        
soma=np.zeros((linhas,colunas))

for i in range (0,soma.shape[0],1):
    for j in range (0,soma.shape[1],1):
        soma[i,j]=a[i,j]+b[i,j]
        
print soma
