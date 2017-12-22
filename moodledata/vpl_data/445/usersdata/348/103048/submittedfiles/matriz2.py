# -*- coding: utf-8 -*-

n = int(input( ' informe a quantidade de linhas/colunas: '))

matriz = []

for i in range (0,n,1):
    matriz2 = []
    for j in range (0,n,1):
        matriz2[i][j] = int(input('informe o %d° linha e o %d° coluna: ' %((i+1),(j+1))))
    matriz.append(matriz2)
print(matriz)
