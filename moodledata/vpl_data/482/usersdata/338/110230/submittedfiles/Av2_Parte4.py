# -*- coding: utf-8 -*-

n = int(input('Número de linhas: '))
m = int(input('Número de colunas: '))
matriz =[]
for i in range(n,0,-1):
    v = []
    for j in range(m,0,-1):
        v.append(int(input('Digite os valores: ')))  
    matriz.append(v)
        
print(matriz)
        
