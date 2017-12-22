# -*- coding: utf-8 -*-
teste1 = False
teste2 = False
dim = int(input(''))
matriz = []

for i in range (dim):
    matriz.append([])
    for j in range(dim):
        matriz[i].append(int(input('')))

atual = 0
anterior = atual
for i in range (dim):
    print(matriz[i])
    anterior = atual
    if anterior == atual:
        teste1 = True
    atual = sum(matriz[i])

atual = 0
for i in range (dim):
    anterior = atual
    if anterior == atual:
        teste2 = True
    soma = 0
    for j in range (dim):
        soma += matriz[i][j]
    atual = soma

diagonal1 = 0
for i in range(dim):
    diagonal1 += matriz[i][i]
diagonal2 = 0
for i in range(dim):
    diagonal2 += matriz[i][dim-i-1]

if teste1 and teste2 and (diagonal1 == diagonal2):
    print('S')
else:
    print('N')
