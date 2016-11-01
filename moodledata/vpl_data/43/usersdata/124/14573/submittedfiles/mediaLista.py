# -*- coding: utf-8 -*-
from __future__ import division

a = 0
b = 0
n = input('Digite o número de valores da lista: ')
I = []
for i in range (0, n, 1):
    I.append(input('Digite um valor para a lista: '))
    a = a + I[b]
    b = b + 1
c = b/len(I)
print(I[0])
print(I[n-1])
print(c)
print(I)