# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz quadrada: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(float(input(' Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
print(matriz)

