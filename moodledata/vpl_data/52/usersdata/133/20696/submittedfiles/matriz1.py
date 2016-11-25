# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def linha1(a):
    for i in range(0, a.shape[0], 1):
        for j in range(0, a.shape[1], 1):
            if a[i,j] == 1:
                break
    return i    


def linha2(a):
    for i in range(a.shape[0] - 1, -1, -1):
        for j in range(0, a.shape[1], 1):
            if a[i,j] == 0:
                break
    return i


def coluna1(a):
    for j in range(0, a.shape[1], 1):
        for i in range(0, a.shape[0], 1):
            if a[i,j] == 1:
                break
    return j

    
def coluna2(a):
    for j in range(a.shape[1], -1, -1):
        for i in range(0, a.shape[0], 1):
            if a[i,j] == 1:
                break
    return j


n = input('Digite o número de linhas da matriz')
m = input('Digite o número de conlunas da matriz')
for i in range(0, n, 1):
    for j in range(0, m, 1):
        a[i,j] = input('Digite o elemento da matriz')
b = linha1(a)
c = linha2(a)
d = coluna1(a)
f = coluna2(a)

print a[b:c+1,d:f+1]
        