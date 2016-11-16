# -*- coding: utf-8 -*-
from __future__ import division

def npico(lista):
    a = 0
    for i in range (0, len(lista)-1, 1):
        if lista[i] >= lista[i+1]:
            a = a + 1
            print(a)
            print(len(lista) - 1)
    if a == len(lista) - 1 or lista[1] <= lista[0]:
        return False
    else:
        return True

n = input('Digite a quantidade de elementos da lista: ')
lista = []
for i in range(0, n, 1):
    lista.append(input('Digite o número de valores da lista: '))

if npico(lista):
    print('S')
else:
    print('N')