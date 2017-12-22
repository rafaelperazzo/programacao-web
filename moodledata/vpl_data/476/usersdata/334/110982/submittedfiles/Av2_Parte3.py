# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de elementos de a: '))
m = int(input('Digite a quantidade de elementos de b: '))

a = []
for i in range(n):
    lista = []
    lista.append(int(input('Digite os elementos de a: ')))
    a.append(lista)

b = []
for i in range(m):
    lista = []
    lista.append(int(input('Digite os elementos de b: ')))
    b.append(lista)

c = 0
for i in range(m):
    if b[i] in a:
        c += 1

print(c)