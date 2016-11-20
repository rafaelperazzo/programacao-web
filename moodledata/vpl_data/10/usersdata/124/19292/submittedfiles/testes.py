# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def minima(a):
    lx = 0
    cx = 0
    li = shape[0]
    ci = shape[1]
    for i in range (0, shape[0], 1):
        for j in range (0, shape[1], 1):
            if a[i,j] == 1:
                if i >= lx:
                    lx = i
                if j >= cx:
                    cx = j
                if i <= li:
                    li = i
                if j <= ci:
                    ci = j
    b = a[li:lx+1,ci:cx+1]
    return b
#COMECE AQUI ABAIXO
linhas = input('Digite a quantidade de linhas: ')
colunas = input('Digite a quantidade de colunas: ')
a = np.zeros( (linhas, colunas) )
for i in range(0, shape[0], 1):
    for j in range(0, shape[1], 1):
        a[i,j] = input('Digite um elemento: ')
        
print minima(a)