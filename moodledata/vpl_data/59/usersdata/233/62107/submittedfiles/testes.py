# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import numpy as np
matriz=np.zeros((10,8))
matriz[2,5]=1
matriz[4,2]=1
matriz[6,2]=1
matriz[7,4]=1
print(matriz)
def menorlinha(L):
    for i in range(0,L.shape[0],1):
        for j in range(0,L.shape[1],1):
            if L[i,j]==1:
                return i
                break
def menorcoluna(L):
    for j in range(L.shape[1]):
        for i in range(L.shape[0]):
            if L[i,j]==1:
                return j
                break
def maiorcoluna(L):
    for j in range(L.shape[1]-1,-1,-1):
        for i in range(L.shape[0]):
            if L[i,j]==1:
                return j
                break
def maiorlinha(L):
    for i in range(L.shape[0]-1,-1,-1):
        for j in range(0,L.shape[1],1):
            if L[i,j]==1:
                return i
                break
corteretangular=matriz[menorlinha(matriz):maiorlinha(matriz)+1,menorcoluna(matriz):maiorcoluna(matriz)+1)
print(corteretangular)