# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    a = 0
    b = 0
    while True:
        for i in range (0, len(lista), 1):
            a = a + 1
            if lista[i + 1] <= lista[1]:
                break
    while True:
        for j in range(i, len(lista), 1):
            b = b + 1
            if lista[j + 1] >= lista[j]:
                break
    if a + b == len(lista) - 1:
        return True
    else:
        return False


n = input('Digite a quantidade de elementos da lista: ')
l = []
for i in range(0, n, 1):
    l.append(input('Digite o número de valores da lista: '))
if pico(l):
    print('S')
else:
    print('N')