# -*- coding: utf-8 -*-
n=int(input('Digite o número de linhas: '))
m=int(input('Digite o número de colunas: '))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,m,1):
        linha.append(int(input('Digite um binario[0,1]: ')))
    matriz.append(linha)
matrizX=[]
for i in range (0,n,1):
    for j in range (0,n,1):
        if matriz[i][j]==1:
            x=i
            break
for i1 in range (n-1,-1,-1):
    for j in range (0,m,1):
        if matriz[i1][j]==1
        x1=i1
        break
for j in range (0,m,1):
    for i in range (0,n,1):
        if matriz[i][j]==1:
            y=j
            break
for j1 in range (m-1,-1,-1):
    for i in range (0,n,1):
        if matriz [i][j1]==1:
            y1=j1
            break
for i in range (x1,x+1,1):
    for j in range (y1,y+1,1):
        matrizX.append(matriz[i][j])
print(matrizX)

