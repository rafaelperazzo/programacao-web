# -*- coding: utf-8 -*-
#entrada
import numpy as np
matriz=[]
m=int(input('digite o numero de linhas da matriz que voceh deseja recortar: '))
n=int(input('digite o numero de colunas da matriz que voceh deseja recortar: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite o valor do elemento da linha%d e da coluna%d desejada: '%((i+1),(j+1)))))
    matriz.append(linha)
linhaszeradas=0
linhaszeradas2=0
colunaszeradas=0
colunaszeradas2=0
#corte superior
for i in range(0,m-1,1) :
    y=sum(matriz[i])
    if y > 0 :
        break
    else :
        linhaszeradas=linhaszeradas+1
if linhaszeradas>0 :
    for i in range(0,linhaszeradas,1):
        del matriz[i]
#corte inferior
for i in range(m-linhaszeradas-1,0,-1) :
    r=int(sum(matriz[i]))
    if r > 0 :
        break
    else :
        linhaszeradas2=linhaszeradas2+1
if linhaszeradas2>0:
    for i in range(m-1,m-linhaszeradas2-1,-1):
        del matriz[i]
t=0
#corte direito
for i in range(0,m-linhaszeradas-linhaszeradas2,1):
    for j in range(0,n,1) :
        if i+1<m-linhaszeradas-linhaszeradas2 :
            t=t+matriz[i][j]+matriz[i+1][j]
            if t > 0 :
                break
            else :
                colunaszeradas=colunaszeradas+1
if colunaszeradas > 0:
    for i in range(0,m-linhaszeradas-linhaszeradas2,1):
        for j in range(0,colunaszeradas,1):
            del matriz[j][i]
#corte esquerdo
f=0
for i in range(0,m-linhaszeradas-linhaszeradas2-1,1):
    for j in range(n-colunaszeradas-1,0,-1) :
        f=f+matriz[i][j]
        if f > 0 :
            break
        else :
            colunaszeradas2=colunaszeradas2+1
if colunaszeradas2>0 :
    for i in range(0,m-linhaszeradas-linhaszeradas2-1,1):
        for j in range(n-colunaszeradas-colunaszeradas2,n-colunaszeradas-colunaszeradas2-1,-1):
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
            
