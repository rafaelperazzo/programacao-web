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
    
