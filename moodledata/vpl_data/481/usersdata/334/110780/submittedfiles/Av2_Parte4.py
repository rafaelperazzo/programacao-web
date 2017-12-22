# -*- coding: utf-8 -*-
n = int(input())

ma = []
for i in range(n):
    for j in range(n):
        lista = []
        lista.append(int(input()))
    ma.append(lista)

for i in range(n):
    for j in range(n):
        cont = 0
        if i == j:
            if sum(a[i]) < a[i][j]:
                cont 