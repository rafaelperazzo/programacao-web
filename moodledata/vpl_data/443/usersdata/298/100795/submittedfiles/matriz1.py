# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de linhas da matriz: '))
n = int(input('Digite a quantidade de colunas da matriz: '))

matriz=[]
for i in range (0, n, 1):
    linha=[]
    for j in range (0, m, 1):
        linha.append(int(input('Digite um elemento para a matriz: ')))
    matriz.append(linha)

matriz2=[]
for i in range (0, n, 1):
    linha2=[]
    for j in range (m-1, -1, -1):
        linha2.append(matriz[i][j])
    matriz2.append(linha2)

print(matriz2)