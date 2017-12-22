# -*- coding: utf-8 -*-

l1 = int(input('Digite a quantidades de elementos da lista 1: '))
lista1 = []
for i in range(0,l1,1):
    lista1.append(int(input('Digite elemento%d: ' % (i+1))))
l2 = int(input('Digite a quantidades de elementos da lista 2: '))
lista2 = []
for i in range(0,l2,1):
    lista2.append(int(input('Digite elemento%d: ' % (i+1))))
print(lista1)
print(lista2)
comuns = lista(set(lista1) & set(lista2)) # ['x', 'c']