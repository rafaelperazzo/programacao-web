# -*- coding: utf-8 -*-
from __future__ import division

def somaDiagonalP(x):
    soma = 0
    for i in range (0, x.shape[0], 1):
        soma = soma + x[i,i]
    return soma

def somaDiagonalS(x):
    soma = 0
    for i in range (0, x.shape[0], 1):
        soma = soma + x[i, x.shape[0]-i-1]
    return soma

def somaLinhas(x):
    s = []
    for i in range(0, x.shape[0], 1):
        soma = 0
        for j in range (0, x.shape[1], 1):
            soma = soma + a[i,j]
        s.append(soma)