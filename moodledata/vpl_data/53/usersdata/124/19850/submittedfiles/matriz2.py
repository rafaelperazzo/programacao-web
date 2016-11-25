# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def magia(a):
    b = 0
    c = 0
    d = 0
    cont = 0
    dp = 0
    ds = 0
    for i in range (0, a.shape[0], 1):
        d = d + a[i,0]
    for i in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            c = c + a[i,j]
        if c == d:
            cont = cont + 1
            c = 0
    for j in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            b = b + a[i,j]
        if b == d:
            cont = cont + 1
            b = 0
    for i in range (0, shape[0], 1):
        for j in range (0, shape[1], 1):
            if i == j:
                dp = dp + a[i,j]
            if i + j == a,shape[0]-1:
                ds = ds + a[i,j]
        if ds == d:
            cont = cont + 1
        if dp == d:
            cont = cont + 1
    if cont == 2*a.shape[0]+2:
        return True
    else:
        return False
        
n = input('Digite o número de linhas e de colunas: ')
a = np.zeros( (n,n) )
for i in range (0, shape[0], 1):
        for j in range (0, shape[1], 1):
            a[i,j] = input('Digite um número: ')
if magia(a):
    print('S')
else:
    print('N')