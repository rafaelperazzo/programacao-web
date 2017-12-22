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
        if i == j:
            ma[i][j] = 0
            sum(ma[i])
            