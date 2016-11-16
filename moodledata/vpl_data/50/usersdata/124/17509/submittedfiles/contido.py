# -*- coding: utf-8 -*-
from __future__ import division

def contido(l1, l2):
    a = 0
    if len(l1) >= len(l2):
        for i in range (0, len(l1), 1):
            for j in range(0, len(l2), 1):
                if l1[i] == l1[j]:
                    a = a + 1
    elif len(l1) < len(l2):
        for i in range (0, len(l2), 1):
            for j in range(0, len(l1), 1):
                if l2[i] == l1[j]:
                    a = a + 1
    return a
    
n = input('Digite o número de valores da lista 1: ')
m = input('Digite o número de valores da lista 2: ')
lista1 = []
lista2 = []
for i in range(0, n, 1):
    lista1.append(input('Digite os valores da lista 1: '))
for i in range(0, m, 1):
    lista2.append(input('Digite os valores da lista 2: '))
    
r = contido(lista1, lista2)
print(r)