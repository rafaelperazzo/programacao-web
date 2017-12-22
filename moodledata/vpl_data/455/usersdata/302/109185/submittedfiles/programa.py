# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz quadrada: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)



