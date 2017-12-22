# -*- coding: utf-8 -*-
m = int(input('informe as linhas: '))
n = int(input('informe as colunas: '))

matriz = []
for i in range (m):
    linhas = []
    for j in range (n):
        linhas.append(int(input('informe os elementos: ')))
    matriz.append(linhas)

print(matriz)
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
    matriz.append(matriz[i][j])
    
print(matriz)
        
