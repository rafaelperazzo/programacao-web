# -*- coding: utf-8 -*-

l1 = int(input('Digite a quantidades de elementos da lista 1: '))
lista1 = []
for i in range(0,l1,1):
    lista1.append(int(input('Digite elemento%d: ' % (i+1))))
print(lista1)

