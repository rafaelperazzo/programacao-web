# -*- coding: utf-8 -*-
m = int(input('informe o numero de linhas: '))
n = int(input('informe o numero de colunas: '))

matriz = []
for i in range (m):
    v = []
    for j in range (n):
        v.append(0)
    matriz.append(v)
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
        matriz[i][j] = int(input('infrome os elementos: '))
print (matriz)