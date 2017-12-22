# -*- coding: utf-8 -*-
#entrada
import numpy as np
matriz=[]
m=int(input('digite o numero de linhas da matriz que voceh deseja recortar: '))
n=int(input('digite o numero de colunas da matriz que voceh deseja recortar: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor do elemento da linha%d e da coluna%d desejada: '%((j+1),(i+1)))))
    matriz.append(linha)
#corte superior
for i in range(0,m,1) :
    y=int(sum(matriz[i])
    if y == 1:
        break
    
'''#corte inferior

#corte direito

#corte esquerdo

#saida'''
print(matriz)
'''matriz=[]
m=int(input('digite o numero de linhas da matriz que voceh deseja recortar: '))
n=int(input('digite o numero de colunas da matriz que voceh deseja recortar: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor do elemento da linha %d desejada: '%(j+1))))
    matriz.append(linha)
indice_superior=m-1
indice_inferior=0
indice_superior=0
indice_superior=n-1
for i in range(0,m,1):
    encontrou_na_linha = False
    for j in range(0,n,1):
        if matriz[i][j]==1 :'''
            
