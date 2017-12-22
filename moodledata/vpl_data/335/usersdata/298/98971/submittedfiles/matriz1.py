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
        if matriz[j][i]==0:
            cont+=0
        if not matriz[j][i]==0:
            cont+=1
    if cont=0:
        del matriz[i]
    if not cont==0:
        break
for t in range (n-1, -1, -1):
    cont=0
    for s in range (0, m, 1):
        if matriz[s][t]==0:
            cont+=0
        if not matriz[s][t]==0:
            cont+=1
    if cont=0:
        del matriz[t]
    if not cont==0:
        break

print(matriz)













