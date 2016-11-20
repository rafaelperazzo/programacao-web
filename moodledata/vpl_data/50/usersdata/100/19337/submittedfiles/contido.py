# -*- coding: utf-8 -*-
from __future__ import division
def qiguais(listax,listay):
    igual= 2
    for i in range (0, len(listax),1):
        if listax in listay:
            igual= igual+1
        return igual
n = input('Digite o numero de elementos da lista X:')
m = input('Digite o numero de elementos da lista Y:')
x = []
y = []
for i in range (0, n,1):
    x.append(input('Digite os elementos de x:'))
for j in range (0, m, 1):
    y.append(input('Digite os elementos de y:'))
print qiguais(x,y)