# -*- coding: utf-8 -*-
n = int(input())

ma = []
for i in range(n):
    for j in range(n):
        lista = []
        lista.append(int(input()))
    ma.append(lista)

cont = 0
for i in range(n):
    for j in range(n):
        if [i] = [j]:
            if sum(ma[i]) < ma[i][j]:
                cont += 1

if cont == n:
    print('SIM')
else:
    print('NAO')