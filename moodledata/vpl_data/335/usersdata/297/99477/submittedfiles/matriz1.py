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
linhaszeradas=0
linhaszeradas2=0
colunaszeradas=0
colunaszeradas2=0
#corte superior
for i in range(0,m,1) :
    y=int(sum(matriz[i]))
    if y == 1 :
        break
    else :
        linhaszeradas=linhaszeradas+1
for i in range(0,linhaszeradas,1):
    del matriz[i]
#corte inferior
for i in range(m-linhaszeradas-1,0,-1) :
    r=int(sum(matriz[i]))
    if r == 1 :
        break
    else :
        linhaszeradas2=linhaszeradas2+1
for i in range(linhaszeradas2,0,-1):
    del matriz[i]
t=0
#corte direito
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(0,j,1) :
        t=t+matriz[i][j]
        if t == 1 :
            break
        else :
            colunaszeradas=colunaszeradas+1
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(0,colunaszeradas,1):
        del matriz[i][j]
#corte esquerdo
f=0
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(n-colunaszeradas,0,-1) :
        f=f+matriz[i][j]
        if f == 1 :
            break
        else :
            colunaszeradas2=colunaszeradas2+1
print(colunaszeradas2)
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(n,n-colunaszeradas2,-1):
        del matriz[i][j]
#saida
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
            
