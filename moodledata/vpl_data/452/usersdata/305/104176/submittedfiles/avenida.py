# -*- coding: utf-8 -*-
matriz = []
M = int(input('Digite o número de quadras no sentido Norte-Sul: '))
while 2 > M or M > 1000:
    M = int(input('Digite o número de quadras no sentido Norte-Sul: '))
N = int(input('Digite o número de quadras no sentido Leste-Oeste: '))
while 2 > N or N > 1000:
    N = int(input('Digite o número de quadras no sentido Leste-Oeste: '))
for i in range (0,M-1,1):
    linha = []
    for j in range (0,N-1,1):
        linha.append(int(input('Digite o valor da respectiva Quadra: ')))
    matriz.append(linha)
    