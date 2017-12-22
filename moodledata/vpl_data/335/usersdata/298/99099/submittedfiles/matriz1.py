# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de linhas da matriz: '))
m = int(input('Digite a quantidade de colunas da matriz: '))

matriz=[]
for l in range (0, n, 1):
    linha=[]
    for i in range (0, m, 1):
        linha.append(int(input('Digite um elemento para a matriz: ')))
    matriz.append(linha)

for i in range (0, n, 1):
    cont=0
    for j in range (0, m, 1):
        if matriz[i][j]==0:
            cont+=0
        if not matriz[i][j]==0:
            cont+=1
    if cont==0:
        del matriz[i]
    if not cont==0:
        break
    
for t in range (n-1, -1, -1):
    cont=0
    for s in range (0, m, 1):
        if matriz[t][s]==0:
            cont+=0
        if not matriz[t][s]==0:
            cont+=1
    if cont==0:
        del matriz[t]
    if not cont==0:
        break

for r in range (0, m, 1):
    cont=0
    for y in range (0, len(matriz), 1):
        if matriz[y][r]==0:
            cont+=0
        if not matriz[y][r]==0:
            cont+=1
    if cont==0:
        del matriz[y][r]
    if not cont==0:
        break

    
for o in range (0, len(matriz), 1):
    cont=0
    for o in range (len(matriz[o])-1, -1, -1):
        if matriz[b][o]==0:
            cont+=0
        if not matriz[b][o]==0:
            cont+=1
    if cont==0:
        del matriz[b][o]
    if not cont==0:
        break

print(matriz)













