# -*- coding: utf-8 -*-
from __future__ import division

def crescente (x):
    cont = 0
    if i == 0:
        if x[i] < x[i + 1]:
        cont = cont + 1
    if cont == x[len(x) - 1]:
        return 'S'
    else:
        return 'N'

def decrescente (y):
    cont = 0
    if i == 0:
        if y[i] > y[i + 1]:
        cont = cont +1
    if cont == a[len(y) - 1]:
        return 'S'
    else:
        return 'N'

def igualdade (z):
    cont = 0
    if i == 0:
        if z[i] == z[i + 1]:
        cont = cont +1
    if cont == z[len(z) - 1]:
        return 'S'
    else:
        return 'N'

n = input("Digite n:")
a = []
b = []
c = []

for i in range (0, n, 1):
    a.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    b.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    c.append(input("Digite um elemento:"))
print def crescente (a)
print def crescente (b)
print def crescente (c)
print def decrescente (a)
print def decrescente (b)
print def decrescente (c)
print def igualdade (a)
print def igualdade (b)
print def igualdade (c)