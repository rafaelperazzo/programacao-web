# -*- coding: utf-8 -*-
import numpy as np
def somadiagonal(matriz):
    soma=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if i==j:
                soma=soma+matriz[i,j]
    return(soma)
def somalinhas(matriz):
    soma=0
    for i in range(matriz.shpe[0]):
        a=soma
        soma=0
        for j in range(matriz.shape[1]):
            soma=soma+matriz[i,j]
        if soma>a:
            soma=soma
        else:
            soma=a
    return(soma)
n=int(input('digite o numero de linhas e colunas da matriz:'))
matriza=np.zeros((n,n))
for i in range(matriza.shapr[0]):
    for j in range(matriza.shape[1]):
        matriza[i,j]=int(input('digite um elemento:'))
if somadiagonal(matriza)>somalinhas(matriza):
    print('SIM')
else:
    print('NAO')