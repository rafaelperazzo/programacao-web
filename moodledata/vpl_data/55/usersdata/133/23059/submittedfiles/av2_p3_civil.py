# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(X, a, b):
    s = 0
    t = 0
    for j in range(0, X.shape[0], 1):
        if(j!=b):
            s = s + X[a,j]
    for i in range(0, X.shape[0], 1):
        if(i!=a):
            t = t + X[i,b]
    p = s + t
    return p
    
    
n = input('Dimensão da matriz:')
x = input('Digite o índice da linha que se deja descobrir o peso:')
y = input('Digite o índice da coluna que se deja descobrir o peso:')
X = np.zeros((n,n))
for i in range(0, n, 1):
    for j in range(0, n, 1):
        print('Elemento X%d,%f' %i%j)
        X[i,j] = input('Valor do elemento:')
print peso(X, x, y)
    