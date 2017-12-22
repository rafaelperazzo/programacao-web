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
            del(ma[i][j])
            sum(ma[i])
            if 