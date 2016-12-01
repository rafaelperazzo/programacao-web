# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def pesoPosicao1(x, y, a):
    j = 0
    if j<(y-1):
        while j<(y-1):
            peso1 = a[x-1,j] + a[x-1,j+1]
            j = j+1
    else:
        peso1 = 0
    return peso1

def pesoPosicao2(x, y, a):
    j = a.shape[1]-1
    if j>(y-1):
        while j>(y-1):
            peso2 = a[x-1,j] + a[x-1,j-1]
            j = j - 1
    else:
        peso2 = 0
    return peso2

def pesoPosicao3(x, y, a):
    i = 0
    if i<(x-1):
        while i<(x-1):
            peso3 = a[i,y-1] + a[i+1,y-1]
            i = j+1
    else:
        peso3 = 0
    return peso3

def pesoPosicao4(x, y, a):
    i = a.shape[0]-1
    if i>(x-1):
        while i>(x-1):
            peso4 = a[i,y-1] + a[i-1,y-1]
            i = i - 1
    else:
        peso4 = 0
    return peso4

def pesoTotal(x, y, a):
    p1 = pesoPosicao1(x, y, a)
    p2 = pesoPosicao2(x, y, a)
    p3 = pesoPosicao3(x, y, a)
    p4 = pesoPosicao4(x, y, a)
    pt = p1 + p2 + p3 + p4
    return pt

n = input("Digite a o valor de n:")
a = np.zeros( (n,n) )
x = input("Digite a linha da posicao:")
y = input("Digite a coluna da posicao:")

for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input("Digite um elemento:")

print ("%d" %pesoTotal(x, y, a))