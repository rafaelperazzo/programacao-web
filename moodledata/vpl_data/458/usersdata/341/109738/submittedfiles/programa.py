# -*- coding: utf-8 -*-
while True:
    n = int(input('Digite a quantidade de linhas e colunas: '))
    if n>2:
        break

matriz = []
for i in range(n):
    v = []
    for j in range(n):
        v.append(int(input('Digite o valor: ')))
    matriz.append(v)
    
mt = []
for i in range (n):
    v = []
    for j in range (n):
        v.append(matriz[j][i])
soma = 0
for i in range(n):
    for j in range(n):
        if (sum(matriz[i])-matriz[i][j]) + (sum(mt[j]) - matriz[i][j]) > soma:
            soma = (sum(matriz[i]) - matriz[i][j]) + (sum(mt[j]) - matriz[i][j])
print(soma)

