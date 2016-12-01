# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def pesoPosicaoL(x, a):
    f = 0
    for j in range(0, a.shape[1], 1):
        f = f + a[x-1, j]
    return f

def pesoPosicaoC(y, a):
    g = 0
    for i in range(0, a.shape[0], 1):
        g = g + a[i,y-1]
    return g
def pesoPosicaoTotal(x, y, a):
    pL = pesoPosicaoL(x, a)
    pC = pesoPosicaoC(y, a)
    pT = pL + pC - 2*a[x-1,y-1]
    return pT

n = input("Digite a o valor de n:")
a = np.zeros( (n,n) )
x = input("Digite a linha da posicao:")
y = input("Digite a coluna da posicao:")

for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input("Digite um elemento:")

print ("%d" %pesoPosicaoTotal(x, y, a))