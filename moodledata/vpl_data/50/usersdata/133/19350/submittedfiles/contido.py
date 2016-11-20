# -*- coding: utf-8 -*-
from __future__ import division

def conta_igual(a, b):
    c = 0
    for i in range(0, len(a), 1):
        for j in range(0, len(b),1):
            if (a[i]==b[j]):
                c = c + 1
    return c

def insere_elemento(lista, n):
    for i in range(0, n, 1):
        lista.append(input('Digite o elemento:')
    return lista
    
n1 = input('Quantidade de elementos de a:')
n2 = input('Quantidade de elementos de b:')
a = [], b = []
print('Preenche a')
a = insere_elemento(a, n1)
print('Preenche b')
b = insere_elemento(b, n2)
c = conta_igual(a, b)
print(c)
