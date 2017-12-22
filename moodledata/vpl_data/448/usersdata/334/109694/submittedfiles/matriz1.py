# -*- coding: utf-8 -*-
import copy

m = int(input())
n = int(input())

ma = []
for i in range (m):
    lista = []
    for j in range (n):
        lista.append(int(input()))
    ma.append(lista)

def rotacionar(matriz):
    nova_matriz = copy.deepcopy(matriz)
    for i in range(len(matriz)):
        nova_matriz[len(matriz)-(i+1)][len(matriz)-(j+1)][len(matriz)-(k+1)] = matriz[i][j]
    return nova_matriz

print(rotacionar(ma))