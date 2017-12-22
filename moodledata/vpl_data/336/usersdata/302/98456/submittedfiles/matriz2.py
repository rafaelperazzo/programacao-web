# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz: '))
matriz = []
for i in range(n):
    linha = []
    linha.append(float(input('Digite a linha%d: ' %i)))
    linha.append(float(input('Digite a linha%d: ' %(i+1))))
    matriz.append(linha)
print(matriz)

