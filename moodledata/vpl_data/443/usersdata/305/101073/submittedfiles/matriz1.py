# -*- coding: utf-8 -*-
matriz = []
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite o valor do %dº elemento da %dº lista: ' %((j + 1),(i + 1)))))
    matriz.append(linha)
for linha in matriz:
    linha.reverse()
matriz.reverse()
print(matriz)