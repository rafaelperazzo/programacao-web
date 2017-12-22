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
        k=int(input('Digite o valor da quadra: '))
        while k<1:
            k=int(input('Entrada invalida. O valor da quadra deve ser pelo menos 1: '))
        while k>100:
            k=int(input('Entrada invalida. O valor da quadra deve ser, no maximo, 100: '))
        linha.append(k)
    matriz.append(linha)

somascolunas=[]
for i in range (0, M, 1):
    coluna=0
    for i in range (0, N, 1):
        coluna+=matriz[N][M]
    somascolunas.append(coluna)

menor=somacolunas[0]
for i in range (1, N, 1):
    if somacolunas[i]<menor:
        menor=somacolunas[i]

print(menor)