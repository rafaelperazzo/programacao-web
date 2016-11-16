# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    a = 0
    b = 0
    i = 0
    while True:
            if lista[i + 1] <= lista[i]:
                break
            else:
                i = i + 1
    while True:
        j = i
        if lista[j + 1] >= lista[j]:
            break
        else:
            j = j + 1
    if j == len(lista) - 1:
        return True
    else:
        return False
    print(j)


n = input('Digite a quantidade de elementos da lista: ')
lista = []
for i in range(0, n, 1):
    lista.append(input('Digite o número de valores da lista: '))
if pico(lista):
    print('S')
else:
    print('N')