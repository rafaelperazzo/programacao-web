# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite a dimensão da Matriz A:  '))
A=np.zeros((n,n))
x=int(input('Digite o índice da linha: '))
y=int(input('Digite o índice da coluna: '))
somalinha=0
somacoluna=0
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=int(input('Digite os pesos em cada posição: '))
for i in range(0,A.shape[0],1):
    for j in range(A.shape[1],1):
        if i==x:
            somalinha=somalinha+A[i,j]
        if j==y:
            somacoluna=somacoluna+A[i,j]
pesoDoIndice=somalinha+somacoluna-2*A[x,y]
print(pesoDoIndice)
    