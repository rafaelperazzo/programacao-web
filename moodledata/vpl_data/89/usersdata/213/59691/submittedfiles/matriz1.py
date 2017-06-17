# -*- coding: utf-8 -*-
def menorLinha(matriz):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if matriz[i,j]==1:
                return (i)

def menorColuna(matriz):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if matriz[i,j]==1:
                return (j)

def maiorLinha(matriz):
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if matriz[i,j]==1:
                return (i)
                
def maiorColuna(matriz):
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if matriz[i,j]==1:
                return (j)
import numpy as np
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))
matriz = np.zeros((linhas,colunas))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Elementos:' ))

recorteMenorLinha=menorLinha(matriz)
recorteMaiorLinha=maiorLinha(matriz)
recorteMenorColuna=menorLinha(matriz)
recorteMenorColuna=maiorLinha(matriz)

print(matriz[recorteMenorLinha:recorteMaiorLinha+1,recorteMenorColuna:recorteMenorColuna+1])