# -*- coding: utf-8 -*-
n = int(input('Digite o número de elementos da lista: '))
a = []
b = []
for i in range(0,n,1):
    a.append(int(input('Digite a%d: ' %(i+1))))
for i in range(0,n,1):
    if i < n and i != 0:
        b.append = a[i-1]-a[i]
        if b.append < 0:
            b.append = -b
