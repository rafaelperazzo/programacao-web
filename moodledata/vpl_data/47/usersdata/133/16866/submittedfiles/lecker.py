# -*- coding: utf-8 -*-
from __future__ import division

def lecker(a):
    cont = 0
    if a[0] > a[1]:
        cont = cont + 1
    if a[len(a)-1] > a[len(a)-2]:
        cont = cont + 1
    for i in range(1, len(a)-1, 1):
        if a[i] > a[i+1] and a[i] > a[i-1]:
        cont = cont + 1
    if cont == 1:
        return True
    else:
        return False

n = input('Digite o número de elementos da lista:')
a = []
b = []
for i in range (0, n, 1):
    a.append(input('Digite o elemento de a:'))
for i in range (0, n, 1):
    b.append(input('Digite o elemento de b:'))

if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print('N')