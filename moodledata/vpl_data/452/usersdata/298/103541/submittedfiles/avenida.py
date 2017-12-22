# -*- coding: utf-8 -*-
M = int(input('Digite o numero de quadras no sentido Norte-Sul: '))
while M<2:
    M = int(input('Entrada invalida. Digite M, sendo M >= 2: '))
while M>1000:
    M = int(input('Entrada invalida. Digite M, sendo M =< 1000: '))
N = int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
while N<2:
    N = int(input('Entrada invalida. Digite N, sendo N >= 2: '))
while N>1000:
    N = int(input('Entrada invalida. Digite N, sendo N =< 1000: '))

matriz=[]
for i in range (0, M, 1):
    linha=[]
    k=0
    for i in range (0, N, 1):
        linha.append(int(input('Digite o valor da quadra: ')))
    matriz.append(linha)

somascolunas=[]
for h in range (0, M-1, 1):
    coluna=0
    for f in range (0, N-1, 1):
        coluna= coluna + matriz[f][h]
    somascolunas.append(coluna)

menor=somascolunas[0]
for i in range (1, N-1, 1):
    if somascolunas[i]<menor:
        menor=somascolunas[i]

print(menor)