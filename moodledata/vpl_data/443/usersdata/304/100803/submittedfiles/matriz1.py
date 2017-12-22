# -*- coding: utf-8 -*-

matriz = []
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite um elemento: ')))
    matriz.append(linha)
print(matriz)