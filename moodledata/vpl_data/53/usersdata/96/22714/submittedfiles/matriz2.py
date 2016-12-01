# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha(a):
    b = []
    for i in range(0,a.shape[0],1):
        soma = 0
        for i in range(0,a.shape[1],1):
            soma = soma + a[i,j]
        b.append(soma)
    return b
    
def somaColunas(a):
    b = []
    for j in range(0,a.shape[1],1):
        soma = 0
        for i in range(0,a.shape[1],1):
            soma = soma + a[i,j]
        b.append(soma)
    return b

def somaDiagonalP(a):
    soma = 0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,j]
    return soma

def somaDiagonalS(a):
    soma = 0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if(i+j)==a.shape[0]-1:
                soma = soma a[i,j]
    return soma
    
def quadradomagico(a):
    sl = somaLinha(a)
    sc = somaColuns(a)
    dp = somaDiagonalP(a)
    ds = somaDiagonalS(a)
    
    contador = 0
    for i in range(0,len(sl),1):
        if dp==ds==sc[i]==sl[i]:
            contador = contador + 1
    
    if contador==len(sl):
        return True
    else:
        return False

n input('Digite o valor de n:')
a = np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j] = input(Digite um valor:')
if quadradomagico(a):
    print('S')
else:
    print('N')