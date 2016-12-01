# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#PROGRAMA PRINCIPAL
linhas=input('Digite o valor de linhas:')


a=pn.zeros((linhas,linhas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        a[i,j]=input('Digite um valor:')

indice1=input('Digite o valor do índice de linhas:')
indice2=input('Digite o valor do índice de colunas:')

soma1=0
for i in range(0,a.shape[0],1):
    soma1=soma1+a[indice1,:]

#soma2=0
#for i in range(0)

print soma1