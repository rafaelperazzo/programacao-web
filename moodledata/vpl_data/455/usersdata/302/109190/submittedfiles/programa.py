# -*- coding: utf-8 -*-
while(True):
    n = int(input('Digite a dimensão da matriz quadrada: '))
    if n >= 3:
        break
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)



