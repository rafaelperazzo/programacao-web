# -*- coding: utf-8 -*-
n = int(input('Quantidade de elementos: '))
lista = []
for i in range (0,3,1):
    v =[]
    for j in range(n):
        v.append(int(input('Digite valor: ')))
    lista.append(v)

for i in range (1,n+1):
    if lista[i-1] > lista[i]:
        print('S')
        if lista[i-1] < lista[i]:
            print('N')