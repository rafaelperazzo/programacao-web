# -*- coding: utf-8 -*-
m = int(input('informe as linhas: '))
n = int(input('informe as colunas: '))

matriz = []
for i in range (m):
    linhas = []
    for j in range (n):
        lnhas.append(0)
matriz.append(linhas)

mt = []
for i in range (m-1,-1,-1):
    linhas = []
    for j in range (n-1,-1,-1):
        linhas.append(int(input('informe os elementos: ')))
    mt.append(linhas)
    
matriz.append(mt)
print(matriz)

