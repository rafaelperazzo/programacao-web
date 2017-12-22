# -*- coding: utf-8 -*-
m = int(input('Informe M: '))
n = int(input('Informe N: '))

matriz = []
for i in range(m):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input('Informe o valor: ')))

matriz2 = []
for i in range(m):
    matriz2.append([])
    for j in range(n):
        matriz2[i].append(matriz[m-i-1][n-j-1])

print(matriz2)
        



