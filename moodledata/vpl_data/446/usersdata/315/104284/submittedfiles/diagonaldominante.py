# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz: '))

matriz = []

for i in range(n):
    v = []
    for j in range(n):
        v.append(int(input('Digite: ')))
    matriz.append(v)
print (matriz)
