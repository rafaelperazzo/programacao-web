# -*- coding: utf-8 -*-
m = int(input())
n = int(input())

ma = []
for i in range (m):
    lista = []
    for j in range (n):
        lista.append(int(input()))
    ma.append(lista)

print(ma)