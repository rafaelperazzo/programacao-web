# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
linha=int(input('Digite a coordenada da linha:'))
coluna=int(input('Digite a coordenada da coluna:'))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]=float(input('Digite o valor de um elemento da matriz:'))

soma1=0
for j in range(0,A.shape[1],1):
    soma1=soma1+A[linha,j]
    
soma2=0
for i in range (0,A.shape[0],1):
    soma2=soma2+A[i,coluna]
resultado=soma1+soma2-(2*A[linha,coluna])
print('%d'%resultado)