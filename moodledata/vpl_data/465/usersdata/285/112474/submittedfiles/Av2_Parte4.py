# -*- coding: utf-8 -*-
n=(int(input('digite a ordem da matriz: ')))
c=>2
matriz=[]
for i in range(0,n,1):
    matriz_linha=[]
    for j in range(0,n,1):
        matriz_linha.append(int(input('digite os elementos: ')))
    matriz.append(matriz_linha)
print(matriz)    
    