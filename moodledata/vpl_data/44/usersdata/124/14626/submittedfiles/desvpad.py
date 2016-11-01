# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
a = 0
d = 0
b = 0
o = 0
n = input('Digite o número de valores da lista: ')
X = []
for i in range (0, n, 1):
    X.append(input('Digite um valor para a lista: '))
    a = a + X[b]
    b = b + 1
c = a/len(X)
for i in range (0, n, 1):
    d = d + (X[o] - c)**2
    o = o + 1
s = (d/(n-1))**(1/2)
print('%.2f' %X[0])
print('%.2f' %X[n-1])
print('%.2f' %c)
print('%.2f' %s)
