# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def minima(a):
    lx = 0
    cx = 0
    li = a.shape[0]
    ci = a.shape[1]
    for i in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            if a[i,j] == 1:
                if i >= lx:
                    lx = i
                if j >= cx:
                    cx = j
                if i <= li:
                    li = 1
                if j <= ci:
                    ci = j
    b = a[li:lx+1, ci:cx+1]
    return b
linhas = input('Digite a quantidade de linhas: ')
colunas = input('Digite a quantidade de colunas: ')
a = np.zeros( (linhas, colunas) )
for i in range (0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input('Digite um elemento: ')
print a
print minima(a)