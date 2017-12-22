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
espelho=[]
for i in range(m,-1,-1):
    espelho.append(matriz[i])
print(espelho)