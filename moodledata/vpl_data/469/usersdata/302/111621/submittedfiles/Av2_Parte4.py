# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)
menor = 1000000000
for i in range(n):
    soma = 0
    for j in range(m):
        soma = soma + matriz[i][j]
    if soma < menor:
        menor = soma
print(menor)