# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)



