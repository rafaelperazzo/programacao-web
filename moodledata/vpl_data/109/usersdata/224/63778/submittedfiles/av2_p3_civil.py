# -*- coding: utf-8 -*-
import numpy as np
def linha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return (soma)
def coluna(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return (soma)

n=int(input('Digite a dimensão da Matriz A:  '))
x=int(input('Digite o índice da linha: '))
y=int(input('Digite o índice da coluna: '))

A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=int(input('Digite os pesos em cada posição: '))
resul=linha(A,x)+coluna(A,y)-(2*A[x,y])
print(resul)