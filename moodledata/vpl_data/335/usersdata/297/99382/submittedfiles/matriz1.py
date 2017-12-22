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
for i in range(0,m,1):
    print(sum(matriz[i]))
    if sum(matriz[i])== 1 :
        break
    else :
        del matriz[i]
print(matriz)
'''#corte inferior
for i in range(m,0,-1):
    s=sum(matriz[i])
    if s == 0 :
        del matriz[i]
    else :
        break
#corte direito
for j in range(0,n,1):
    t=sum(matriz[j])
    if t == 0 :
        del matriz[j]
    else :
        break
#corte esquerdo
for j in range(n,0,-1):
    r=sum(matriz[j])
    if r == 0 :
        del matriz[j]
    else :
        break
#saida
print(matriz)'''
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
            
