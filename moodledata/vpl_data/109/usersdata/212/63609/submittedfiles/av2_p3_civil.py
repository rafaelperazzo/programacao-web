# -*- coding: utf-8 -*-
import numpy as np
x=int(input('Ccoloque o numero de linhas e colunas:'))
matriz=np.zeros((x,x))
for i in range(0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]=int(input('Digite um elemento da matriz:'))
l=int(input('Digite a linha:'))
c=int(input('Digite a coluna:'))
soma=0
for i in range (0,matriz.shape[0],1):
    soma=soma+matriz[i,c]
soma=soma-matriz[l,c]
for j in range (0,matriz.shape[1],1):
    soma=soma+matriz[l,j]
soma=soma-matriz[l,c]
print(soma)
