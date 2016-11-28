# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def matrix(a,b):
    i = 0
    j = 0
    c = np.zeros((l,c))
    while (l-1)>=i:
        while (c-1)>=j:
            c[i,j] = a[i,j]+b[i,j]
            j = j+1
        i = i+1
        j = 0
    return c

l = input('Digite o número de linhas da matriz: ')
c = input('Digite o número de coluas da matriz: ')

m = np.zeros((l,c))

i = 0
j = 0

while (l-1)>=i
    m[i,j] = input('Digite o valor: ')
    i = i+1

print m