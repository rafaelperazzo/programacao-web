# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def pesoPosicaoX(x, y, a):
    for j in range(0, y-1, 1):
        peso = a[x-1,j] + a[x-1,j+1]
    return peso

def pesoPosicaoY(x, y, a):
    f = a.shape[0]-1
    for i in range(0, x-1, 1):
        peso = a[i,y-1] + a[i+1,y-1]
    return peso

def pesoTotal(x, y, a):
    px = pesoPosicaoX(x, y, a)
    py = pesoPosicaoY(x, y, a)
    pt = px + py
    return pt

n = input("Digite a o valor de n:")
a = np.zeros( (n,n) )
x = input("Digite a linha da posicao:")
y = input("Digite a coluna da posicao:")

for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input("Digite um elemento:")

print ("%d" %pesoTotal(x, y, a))