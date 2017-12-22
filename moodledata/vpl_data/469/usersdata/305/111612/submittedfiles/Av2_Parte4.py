# -*- coding: utf-8 -*-
matriz = []
m = int(input('Digite o número de quadras no sentido N-S: '))
n = int(input('Digite o número de quadras no sentido L-O: '))
while m < 2 or m > 1000:
    m = int(input('Digite o número de quadras no sentido N-S: '))
for i in range (0,m,1):
    linha = []
while n < 2 or n > 1000:
    n = int(input('Digite o número de quadras no sentido L-O: '))
for j in range (0,n,1):
    linha.append(int(input('Digite o valor da quadra: ')))
    matriz.append(linha)
print(matriz)    