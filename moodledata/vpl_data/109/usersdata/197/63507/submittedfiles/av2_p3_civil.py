# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]=float(input('Digite o valor de um elemento da matriz:'))
x=float(input('Digite sua coordenada:'))
linha=x//10
coluna=x%10
soma1=0
for j in range(0,A.shape[1],1):
    soma1=soma1+A[linha,j]
    
soma2=0
for i in range (0,A.shape[0],1):
    soma2=soma2+A[i,coluna]
resultado=soma1+soma2-(2*A[linha,coluna])
print('%d'%resultado)
print(A)
print(soma1)
print(linha)
print(coluna)
print(soma2)
    