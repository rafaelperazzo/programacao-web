# -*- coding: utf-8 -*-
import numpy
m = []
n = int(input('Digite a dimensão da matriz: '))
for i in range(0,n,1):
    l = []
    for j in range(0,n,1):
        l.append(int(input('Digite um valor de c ')))
    m.append(l)
print(m)    