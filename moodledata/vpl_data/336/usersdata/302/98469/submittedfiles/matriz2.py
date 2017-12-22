# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz: '))
matriz = []
for i in range(n):
    linha = []
    linha.append(float(input('Digite a linha: ')))
    linha.append(float(input('Digite a linha: ')))
    matriz.append(linha)
print(matriz)
for i in range(n-1):
    if sum(matriz[i][0]) == sum(matriz[i+1][0]):
        print(sum(matriz[i][0])
