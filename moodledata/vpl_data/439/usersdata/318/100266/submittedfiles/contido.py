# -*- coding: utf-8 -*-

l1 = int(input('Digite a quantidades de elementos da lista 1: '))
l2 = int(input('Digite a quantidades de elementos da lista 2: '))
lista1 = []
for i in range(0,l1,1):
    lista1.append(int(input('Digite elemento da lista 1%d: ' % (i+1))))
lista2 = []
for i in range(0,l2,1):
    lista2.append(int(input('Digite elemento da lista  2%d: ' % (i+1))))
comuns = []
for i in lista1:
    if(i in lista2):
        comuns.append(i)
print(len(comuns))
