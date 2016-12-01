# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#PROGRAMA PRINCIPAL
indice1=input('Digite o valor do índice de linhas:')
indice2=input('Digite o valor do índice de colunas:')

n=input('Digite o sumero de linhas e colunas:')

a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        a[i,j]=input('Digite um valor:')

soma1=0
for i in range(0,a.shape[0],1):
    soma1=soma1+a[indice1,i]

soma2=0
for i in range(0,a.shape[0],1):
    soma2=soma2+a[indice2,i]

somatorio=(soma1+soma2)-2*a[indice1,indice2]

print somatorio