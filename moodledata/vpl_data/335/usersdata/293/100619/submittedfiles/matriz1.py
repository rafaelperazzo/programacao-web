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
print(matriz)
###VERIFICAR LINHAS NULAS###

for i in range(len(matriz)-1,-1,-1):
    cont_linhas=0
    for j in range(0,n,1):
        if matriz[i][j]==0:
            cont_linhas= cont_linhas + 1
    if cont_linhas>0:
        matriz.pop(i)
###COLUNAS NULAS###

for j in range(n-1,-1,-1):
    cont_colunas=0
    for i in range(len(matriz)-1,-1,-1):
        if matriz[i][j]==0:
            cont_colunas= cont_colunas+ 1
    if cont_colunas>0:
        for k in range(0,len(matriz)-1,-1):
            matriz[k].pop(j)
print(matriz)