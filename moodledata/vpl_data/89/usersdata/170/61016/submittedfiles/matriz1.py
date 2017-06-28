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
        for j in range

