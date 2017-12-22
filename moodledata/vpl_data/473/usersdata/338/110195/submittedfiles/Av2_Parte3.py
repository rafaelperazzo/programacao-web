# -*- coding: utf-8 -*-
n = int(input('Quantidade de elementos: '))
lista = []
for i in range (0,n,1):
    v =[]
    for j in range(n):
        v.append(int(input('Digite valor: ')))
    lista.append(v)
print(lista)