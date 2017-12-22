# -*- coding: utf-8 -*-
n = int(input('número de linhas e colunas da matriz: '))
matriz = []
for i in range(n) :
    elementos = []
    for j in range(n) :
        elementos.append(int(input('elementos da matriz: ')))
    matriz.append(elementos)
x = 0
for i in range(0,1,1) :
    x = x + matriz[0][1] + matriz[0][0+i]

print(x)