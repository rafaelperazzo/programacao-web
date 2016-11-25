# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def diagonalp(a):
    s = 0
    for i in range(0, a.shape[0], 1):
        s = s + a[i,i]
return s


def diagonals(a):
    s = 0
    for i in range(0, a.shape[0],1):
        s = s + a[i,a.shape[0]-1-i]
return s


def samalinha1(a):
    s = []
    for i in range(0, a.shape[0], 1):
        s[i] = 0
    for i in range(0, a.shape[0], 1):
        for j in range(0, a.shape[0], 1):
            s[i]= s[i] + a[i,j]
    return s


def somacoluna1(a):
    s = []
    for i in range(0, a.shape[0], 1):
        s[i] = 0
    for j in range(0, a.shape[0], 1):
        for i in range(0, a.shape[0], 1):
            s[j] = s[j] + a[i,j]

    return s

def somalinha(a):
    c = []
    for i in range(0, a.shape[0], 1):
        soma = 0
        for j in range(0, a.shape[0], 1):
            soma = soma + a[i,j]
        c.append(soma)
    return c
    
def somacoluna(a):
    c = []
    for j in range(0, a.shape[0], 1):
        soma = 0
        for i in range(0, a.shape[0], 1):
            soma = soma + a[i,j]
        c.append(soma)
    return c

def verifica(a):
    b = diagonalp(a)
    c = diagonals(a)
    d = somalinha(a)
    e = somalinha(a)
    
    for i in range(0, len(d), 1):
        if d[0]!=d[i]:
            return False
    
    for i in range(0, len(e), 1):
        if e[0]!=e[i]:
            return False
    
    if b == c and b==c and b == d[0] and b == e[0]:
        return True
    else:
        return False
        
        
n = input('Dimensão da matríz:')
a = np.zeros((n,n))
for i in range(0, n, 1):
    for j in range(0, n, 1):
        a[i,j]= input('Digíte um elemento da matríz')
        
if verifica(a):
    print('S')
else:
    print('N')
        
        