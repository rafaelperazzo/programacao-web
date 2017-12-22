# -*- coding: utf-8 -*-
m=int(input(''))
n=int(input(''))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
print(matriz)
matriz2=[]
for i in range(m-1,-1,-1):
    matriz2.append(matriz[i])
print(matriz2)
espelho=[]
for i in range(0,m,1):
    for j in range(n-1,-1,-1):
        espelho.append(matriz2[i][j])
print(espelho)
        
print(espelho)