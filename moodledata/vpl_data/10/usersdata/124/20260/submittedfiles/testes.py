# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def sistemalinear(a, x, b):
    d = np.zeros( (a.shape[0], 1) )
    c = 0
    l = 0
    for i in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            c = c + a[i,j]*x[j,i]
        d[l,0] = c
        c = 0
        l = l + 1
    if b == d:
        return True
    else:
        return False

d = input('Digite o número de linhas e de colunas: ')
a = np.zeros( (d,d) )
x = np.zeros( (d,1) )
b = np.zeros( (d,1) )
for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input('Digite um valor para a matriz a: ')
for i in range(0, x.shape[0], 1):
    for j in range(0, x.shape[1], 1):
        x[i,j] = input('Digite um valor para a matriz x: ')
for i in range(0, b.shape[0], 1):
    for j in range(0, b.shape[1], 1):
        b[i,j] = input('Digite um valor para a matriz b: ')
        
if sistemalinear(a, x, b):
    print('Sim')
else:
    print('Não')