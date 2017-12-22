# -*- coding: utf-8 -*-
def primeira linha(matriz):
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            if matriz[i,j] ==1:
                return(i)
                
def primeiracoluna(matriz):
    for j in range(0,matriz.shape[1],1):
        for i in range(0,matriz.shape[0],1):
            if matriz[i,j] ==1:
                return(j)
                
def ultimacoluna(matriz):
    for j in range(matriz.shape[1] -1,-1,-1):
        for i in range(matriz.shape[0]-1,-1,-1):
            if matriz[i,j]==1:
                return(j)
                
def ultimalinha(matriz):
    for i in range(matriz.shape[0]-1,-1,-1):
        for j in range(matriz.shape[1]-1,-1,-1):
            if matriz[i,j]==1:
                return(i)
                
linhas=int(input(
