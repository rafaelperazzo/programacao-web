# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    c = 0
    d = 0
    for i in range(0, len(lista)-1, 1):
        c = lista[i] - lista[i+1]
        if c < 0:
            c = c*(-1)
        if c > d:
            d = c
    return d
    
n = input('Digite a quantidade de valores da lista: ')
l = []
for i in range(0, n, 1):
    l.append(input('Digite um valor para a lista: ')
print degrau(l)