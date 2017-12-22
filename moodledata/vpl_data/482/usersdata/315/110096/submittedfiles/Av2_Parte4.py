# -*- coding: utf-8 -*-
m = int(input('Digite M: '))
n = int(input('Digite N: '))

matriz = []

for i in range(m):
    v = []
    for j in range(n):
        v.append(int(input('Digite valor: ')))
    matriz.append(v)

mespelhada = []
for i in range(m-1, -1, 1):
    v = []
    for j in range (n-1, -1, 1):
        v.append(matriz[i][j])
    mespelhada.append(v)
    
print(matriz)
print(mespelhada)







