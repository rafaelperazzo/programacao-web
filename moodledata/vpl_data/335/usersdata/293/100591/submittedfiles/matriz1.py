# -*- coding: utf-8 -*-
import numpy as np
###CRIAR MATRIZ###
matriz=[]

m=int(input("Digite o número de linhas da lista: "))
n=int(input("Digite o número de colunas da lista: "))

for i in range(0,m,1):
    matriz_linha=[]
    for j in range(0,n,1):
        matriz_linha.append(int(input("Digite o valor do elemento (%d,%d): "%(i+1,j+1))))
    matriz.append(matriz_linha)
###VERIFICAR LINHAS NULAS###
cont=0
for i in range(0,m,1):
    for j in range(0,n,1):
        if matriz[i][j]==0:
            cont= cont + 1
    if cont==0:
        matriz.pop([i][j])
print(matriz)        