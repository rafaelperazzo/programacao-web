# -*- coding: utf-8 -*-
matriz=[]
m=int(input("digite o valor de linhas: "))
n= int(input('digite o valor de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os elementos%d: '%(i+1))))
    matriz.append(linha)
print(matriz)
matrizB=[]
for i in range(m-1,m,-1):
    linha=[]
    for j in range(n-1,-1,-1):
        lista.append(matriz[i][j])
    matrizB.append(lista)
print(matrizB)
