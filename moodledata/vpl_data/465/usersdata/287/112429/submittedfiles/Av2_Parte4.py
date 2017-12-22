# -*- coding: utf-8 -*-
matriz=[]
n=int(input('digite n da matriz quadrada: '))
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('digite os valores da matriz: ')))
        matriz.append(linha)
print(matriz)
