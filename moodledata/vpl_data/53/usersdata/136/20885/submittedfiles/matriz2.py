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
    return s

def somaColunas(x):
    s = []
    for i in range(0, x.shape[0], 1):
        s.append(sum(x[i,:]))
    return s

def quadradoMagico(x):
    sd1 = somaDiagonalP(x)
    sd2 = somadiagonalS(x)
    
    somaL = somaLinhas(x)
    somaC = somaColunas(x)
    
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