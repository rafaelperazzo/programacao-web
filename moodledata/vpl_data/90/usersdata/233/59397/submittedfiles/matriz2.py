# -*- coding: utf-8 -*-
import numpy as np
def somasecundaria(matriz):
    soma=0
    j=0
    i=lista.shape[0]-1
    while j<matriz.shape[1]:
        soma=soma+matriz[i,j]
        j=j+1
        i=i-1
    return soma
n=int(input('Digite o número de linhas e colunas da matriz: '))
matriza=np.zeros((n,n))
for i in range(matriza.shape[0]):
    for j in range(matriza.shape[1]):
        matriza[i,j]=int(input('Digite um número: '))
print(matriza)
print(somasecundaria(matriza))
