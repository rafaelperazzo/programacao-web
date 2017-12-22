# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))
matriz = []
matriz2 = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        matriz2.append(matriz[i][j])
print(matriz2)
        

