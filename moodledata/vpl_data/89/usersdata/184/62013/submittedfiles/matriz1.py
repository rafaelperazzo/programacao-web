# -*- coding: utf-8 -*-
import numpy as np
def menorlinha(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i,j]==1:
                return (i)
def menorcoluna(matriz):
    for j in range(matriz.shape[1]):
        for i in range(matriz.shape[0]):
            if matriz[i,j]==1:
                return(j)
def maiorlinha(matriz):
    for i in range(matriz.shape[0]-1,-1,-1):
        for j in range(matriz.shape[1]):
            if matriz[i,j]==1:
                return(i)
def maiorcoluna(matriz):
    for i in range(matriz.shape[1]-1,-1,-1):
        for i in range(matriz.shape[0]):
            if matriz[i,j]==1:
                return(j)
n=int(input('digite o número de linhas da matriz:'))
m=int(input('digite o número de colunas da matriz:'))
matriza=np.zeros((n,m))
for i in range(n):
    for j in range(m):
        matriza[i,j]=int(input('digite o zero     :'))
print(matriza[menorlinha(matriza):maiorlinha(matriza):menorcoluna(matriza):maiorcoluna(matriza)])


