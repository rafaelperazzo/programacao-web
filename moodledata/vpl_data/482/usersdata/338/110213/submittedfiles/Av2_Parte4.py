# -*- coding: utf-8 -*-

n = int(input('Número de linhas: '))
m = int(input('Número de colunas: '))
matriz =[]
for i in range (-1,n-1,-1):
    for j in range (-1,m-1,-1):
        matriz.append(int(input('Digite os valores: ')))
        
print(matriz)
        
