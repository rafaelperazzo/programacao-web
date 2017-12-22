# -*- coding: utf-8 -*-
#entrada
import numpy as np
m=int(input('digite o numero de linhas da matriz que voceh deseja recortar: '))
n=int(input('digite o numero de colunas da matriz que voceh deseja recortar: '))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor do elemento da linha %d desejada: '%(j+1))))
    matriz.append(linha)
#corte superior
print(matriz[i])
for i in range(0,m,1):
    if sum(matriz[i])==0 :
        del matriz[i]
    else :
        break
#corte inferior
for i in range(m,0,-1):
    if sum(matriz[i])==0 :
        del matriz[i]
    else :
        break
#corte direito
for j in range(0,n,1):
    if sum(matriz[j])==0 :
        del matriz[j]
    else :
        break
#corte esquerdo
for j in range(n,0,-1):
    if sum(matriz[j])==0 :
        del matriz[j]
    else :
        break
#saida
print(matriz)