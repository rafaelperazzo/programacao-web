# -*- coding: utf-8 -*-

n = int(input('Número de linhas: '))
m = int(input('Número de colunas: '))
matriz =[]
for i in range(n,0,-1):
    for j in range(m,0,-1):
        matriz.append(int(input('Digite os valores: ')))
        
print(matriz)
        
