# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz: '))
matriz = []
for i in range(n):
    v = []
    for j in range(n):
        v.append(int(input('Digite: ')))
    matriz.append(v)
soma = 0
for i in range (n):
    if matriz[i][i] >= sum(matriz[i]) - matriz[i][i]:
        soma += 1
if soma == n:
    print('SIM')
else:
    print('NAO')