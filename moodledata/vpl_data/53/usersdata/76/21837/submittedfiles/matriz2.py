# -*- coding: utf-8 -*-
from __future__ import division

def somaDiagonal1(a):
    soma = 0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,i]
    return soma

def somaDiagonal2(a):
    soma = 0
    i = 0
    j = a.shape[0]-1
    while i<a.shape[0]:
        soma = soma + a[i,j]
        i = i + 1
        j = j - 1
    return soma

def somaLinhas(a):
    s = []
    for i in range(0,a.shape[0],1):
        soma = 0
        for j in range(0,a.shape[1],1):
            soma = soma + a[i,j]
        s.append(soma)
    return soma
def somaColunas(a):
    s = []
    for j in range(0,a.shape[1],1):
        soma = 0
        for i in range(0,a.shape[0],1):
            soma = soma + a[i,j]
        s.append(soma)
    return soma