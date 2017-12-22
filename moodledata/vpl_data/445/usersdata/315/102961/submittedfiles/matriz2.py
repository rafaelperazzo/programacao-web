# -*- coding: utf-8 -*-
n = int(input('digite quant de linhas e colunas da matriz: '))

matriz = []
for i in range(0,n,1):
    
    for j in range(0,n,1):
        vetor = []
        vetor[i][j] = (int(input('digite: '))
    matriz.append(vetor)
    
print(matriz[2][2])
