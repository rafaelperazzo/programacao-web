# -*- coding: utf-8 -*-
from __future__ import division

def npico(lista):
    a = 0
    for i in range (0, len(lista)-1, 1):
        if lista[i] > lista[i+1]:
            a = i
            break
    if a != 0:
        cont = 0
        for i in range(a, len(lista)-1, 1):
            if lista[i]<=lista[i+1]:
                cont = cont + 1
        if cont == 0:
            return True
        else:
            return False
    else:
        return False

n = input('Digite a quantidade de elementos da lista: ')
lista = []
for i in range(0, n, 1):
    lista.append(input('Digite o número de valores da lista: '))

if npico(lista):
    print('S')
else:
    print('N')