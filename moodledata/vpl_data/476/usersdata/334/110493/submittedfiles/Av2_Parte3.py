# -*- coding: utf-8 -*-
n = int(input())
m = int(input())

a = []
for i in range(n):
    lista = []
    lista.append(int(input()))
    a.append(lista)

b = []
for i in range(m):
    lista = []
    lista.append(int(input()))
    b.append(lista)

c = 0
for i in range(m):
    if b[i] in a:
        c += 1

print(c)