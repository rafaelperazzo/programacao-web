# -*- coding: utf-8 -*-
m = int(input('informe o numero de linhas: '))
n = int(input('informe o numero de colunas: '))

matriz = []
for i in range (m):
    linhas = []
    for j in range (n):
        linhas.append(int(input('informe os elementos: ')))
    matriz.append(linhas)
print(matriz)
