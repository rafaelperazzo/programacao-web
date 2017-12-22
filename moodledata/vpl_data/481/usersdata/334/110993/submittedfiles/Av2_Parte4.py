# -*- coding: utf-8 -*-
n = int(input('Insira a ordem da matriz: '))

ma = []
for i in range(n):
    lista = []
    for j in range(n):
        lista.append(int(input('Insira os elementos da matriz: ')))
    ma.append(lista)

cont = 0
for i in range(n):
    for j in range(n):
        if i == j:
            if sum(ma[i])-ma[i][j] < ma[i][j]:
                cont += 1

if cont == n:
    print('SIM')
else:
    print('NAO')