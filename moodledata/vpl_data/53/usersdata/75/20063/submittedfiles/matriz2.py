# -*- coding: utf-8 -*-
import numpy as np

linhas=input('Digite a quantidade de linhas da matriz:')
colunas=input('Digite a quantidade de colunas da matriz:')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')