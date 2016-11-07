# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    c = 0
    if lista[0] > lista[1]:
        c = c + 1
        if lista[len(lista) - 1] >lista[len(lista) - 2]:
            c = c + 1
            for i in range(1, n - 1, 1):
                if lista[i] > lista[i + 1] and lista[i] > lista[i - 1]:
                    c = c + 1
    if c > 1 or c == 0:
        return True
    else:
        return False
n = input('Digite o número de valores das listas: ')
a = []
b = []
for i in range (0, n, 1):
    a.append(input('Digite os valores de a: '))
for i in range (0, n, 1):
    b.append(input('Digite os valores de b: '))

if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print('N')