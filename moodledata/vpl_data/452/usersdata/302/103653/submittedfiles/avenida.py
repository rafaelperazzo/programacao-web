# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('DIgite o número de colunas: '))
while(n < 2 or n > 1000 or m < 2 or m > 1000):
    m = int(input('Digite o número de linhas: '))
    n = int(input('DIgite o número de colunas: '))
    break
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
        matriz.append(linha)
print(matriz)
