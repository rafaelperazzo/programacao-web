# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
m= 3
n= 4
matriz= []
for i in range (0,m,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input('Digite os elementos da linha%d: ' %(i+1))))
    matriz.append(linha)
for j in range (0,n,1):
    soma=0
    for i in range (0,m,1):
        soma+=matriz[i][j]