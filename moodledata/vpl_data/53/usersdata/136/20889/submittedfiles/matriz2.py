# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaDiagonalP(a):
    soma = 0
    for i in range (0, a.shape[0], 1):
        soma = soma + a[i,i]
    return soma

def somaDiagonalS(a):
    soma = 0
    for i in range (0, a.shape[0], 1):
        soma = soma + a[i, a.shape[0]-i-1]
    return soma

def somaLinhas(a):
    s = []
    for i in range(0, a.shape[0], 1):
        soma = 0
        for j in range (0, a.shape[1], 1):
            soma = soma + a[i,j]
        s.append(soma)
    return s

def somaColunas(a):
    s = []
    for i in range(0, a.shape[0], 1):
        s.append(sum(a[i,:]))
    return s

def quadradoMagico(a):
    sd1 = somaDiagonalP(a)
    sd2 = somaDiagonalS(a)
    
    somaL = somaLinhas(a)
    somaC = somaColunas(a)
    
    cont = 0
    for i in range(0, len(somaL), 1):
        if sd1==sd2==somaL[i]==somaC[i]:
            cont = cont + 1
        
    if cont == len(somaL):
        return True
    else:
        return False

n = input("Digite n:")
a = np.zeros( (n,n) )

for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j] = input("Digite um elemento:")

if quadradoMagico(a):
    print('S')
else:
    print('N')