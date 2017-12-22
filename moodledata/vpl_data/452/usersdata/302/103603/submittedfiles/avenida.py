# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('DIgite o número de colunas: '))
matriz = []
while(True):
    if n>=2 and n <= 1000 and m>=2 and m>=1000:
        for i in range(m):
            linha = []
            for j in range(n):
                linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
            matriz.append(linha)
        print(matriz)
