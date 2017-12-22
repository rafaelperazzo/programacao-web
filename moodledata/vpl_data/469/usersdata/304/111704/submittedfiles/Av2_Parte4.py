# -*- coding: utf-8 -*-
m = int(input('Coluna: '))
n = int(input('Linha: '))
matriz = []
for i in range (0,n,1):
    linha=[]
    for j in range (0,m,1):
        linha.append(int(input('Linha: ')))
    matriz.append(linha)
print(matriz)