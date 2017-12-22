# -*- coding: utf-8 -*-
matriz = []
m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
print(matriz)

        

