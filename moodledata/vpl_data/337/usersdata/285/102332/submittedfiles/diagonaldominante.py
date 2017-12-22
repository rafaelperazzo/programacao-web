# -*- coding: utf-8 -*-
a=int(input("digite a ordem da matriz: "))
while(True):
    if a<2:
        a=int(input("digite a ordem da matriz: "))
    else:
        break
matriz=[]
for i in range(0,a,1):
    matriz_linha=[]
    for j in range(0,a,1):
        matriz_linha.append(int(input("digite o elemento(%d,%d): "%(i+1,j+1))))
    matriz.append(matriz_linha)
soma_dp=0
for i in range(0,a,1):
    for j in range(0,a,1):
        if i==j:
            soma_dp=matriz[i][j]+soma_dp
cont=0
for i in range(0,a,1):
    if sum(matriz[i])>soma_dp
        cont=cont+1
for j in range(0,a,1):
    soma_colunas=0
    for i in range(0,a,1):
