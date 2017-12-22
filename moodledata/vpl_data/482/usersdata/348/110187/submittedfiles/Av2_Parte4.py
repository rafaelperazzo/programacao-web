# -*- coding: utf-8 -*-
m = int(input('informe as linhas: '))
n = int(input('informe as colunas: '))

matriz = []
for i in range (m):
    linhas = []
    for j in range (n):
        linhas.append(int(input('informe os elementos: ')))
    matriz.append(linhas)

mt = []
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
        linhas.append(int(input('informe os elementos: ')))
    mt.append(linhas)
    
m = [ 2,3,4]
for i in range (4-1,-1,-1):
    m[i]
    
print(m)


