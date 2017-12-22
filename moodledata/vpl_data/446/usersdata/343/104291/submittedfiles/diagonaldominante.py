# -*- coding: utf-8 -*-
n = int(input('número de linhas e colunas da matriz: '))
matriz = []
for i in range(n) :
    elementos = []
    for j in range(n) :
        elementos.append(int(input('elementos da matriz: ')))
    matriz.append(elementos)
x = 0
x += matriz[0][j]
print(x)