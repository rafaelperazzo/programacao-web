# -*- coding: utf-8 -*-
m = int(input('Digite quantidade de linhas: '))
n = int(input('Digite quantidade de colunas: '))
matriz = []
for i in range(m):
    vetor = []
    for j in range(n):
        vetor.append(0)
    matriz.append(vetor)
for i in range (m-1, -1, -1):
    for j in range (n-1, -1, -1):
        matriz[i][j] = int(input('Digite um valor: '))
    print(matriz)


