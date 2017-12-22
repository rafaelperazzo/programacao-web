# -*- coding: utf-8 -*-
n = int(input('informe o tamanho da MATRIZ: '))

matriz = []
for i in range (n):
    linhas = []
    for j in range (n):
        linhas.append(int(input( 'informe os elementos: ')))
    matriz.append(linhas)
print(matriz)
