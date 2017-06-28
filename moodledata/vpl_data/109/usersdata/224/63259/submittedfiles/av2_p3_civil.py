# -*- coding: utf-8 -*-
import numpy as np
def somatórioDaColuna(A,j):
    soma2=0
    for i in range(0,A.shape[0],1):
        soma2=soma2+1
    return(soma2)
    
def somatórioDaLinha(A,i):
    soma=0
    for j in range(0,A.shape[1],1):
        soma=soma+A[i,j]
    return (soma)
def resultado(A,x,y):
    resultado=somatórioDaColuna(A,y)
n=int(input('Digite a dimensão da Matriz A:  '))
x=int(input('Digite o índice da linha: '))
y=int(input('Digite o índice da coluna: '))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1]1):
        A[i,j]=int(input('Digite os pesos em cada posição: '))


