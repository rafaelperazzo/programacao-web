# -*- coding: utf-8 -*-
import numpy as np
def menorlinha(matriz):
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if matriz[i,j]==1:
                return (i)
def maiorlinha(matriz):
    for i in range(matriz.shape[0]-1,-1,-1):):
        for j in range(matriz.shape[1]):
            if matriz[i,j]==1:
                return(i)
def menorcoluna(matriz):
    for j in range(matriz.shape[1]):
        for i in range(matriz.shape[0]):
            if matriz[i,j]==1:
                return(j)
def maiorcoluna(matriz):
    for j in range(matriz.shape[1]-1,-1,-1):):
        for i in range(matriz.shape[0]):
            if matriz[i,j]==1:
                return(j)
n=int(input('n:'))
m=int(input('n:'))
matrizA=np.zeros((n.m))
for i in range(n):
    for j in range(m):
        matrizA[i,j]=int(input('zero ou um'))
print(matrizA[menorlinha(matrizA):maiorlinha(matrizA)+1,menorcoluna(matrizA):maiorcoluna(matrizA)+1])

    
            

