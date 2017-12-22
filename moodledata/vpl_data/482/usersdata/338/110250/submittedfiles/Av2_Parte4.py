# -*- coding: utf-8 -*-

n = int(input('Número de linhas: '))
m = int(input('Número de colunas: '))
matriz =[]
for i in range(-1,1-n,-1):
    v = []
    for j in range(-1,1-n,-1):
        v.append(int(input('Digite os valores: ')))  
    matriz.append(v)
        
print(matriz)
"""        
n = int(input('Número de linhas: '))
for i in range (n,0,-1):
    print(i)
"""