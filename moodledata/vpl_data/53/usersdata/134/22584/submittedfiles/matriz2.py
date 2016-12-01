# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiag1(a):
    soma = 0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,i]
    return soma

def somadiag2(a):
    soma = 0
    i = 0
    j = a.shape[0]-1
    while i < a.shape[0]:
        soma = soma + a[i,j]
        i = i + 1
        j = j - 1
    return soma
    
def somalin(a):
    s = []
    for i in range(0,a.shape[0],1):
        soma = 0
        for j in range(0,a.shape[1],1):
            soma = soma + a[i,j]
        s.append(soma)
    return s

def somacol(a):
    s = []
    for j in range(0,a.shape[1],1):
        soma = 0
        for i in range(0,a.shape[0],1):
            soma = soma + a[i,j]
        s.append(soma)
    return s
    
def quadradomagico(a):
    sd1 = somadiag1(a)
    sd2 = somadiag2(a)
    somaL = somalin(a)
    somaC = somacol(a)
    cont = 0
    for i in range(0,len(somaL),1):
        if sd1 == sd2 == somaL[i] == somaC[i]:
            cont = cont + 1
    if cont == len(somaL):
        return True
    else:
        return False
    
    
#PROGRAMA PRINCIPAL

n = input('Digite as dimensões da matriz:')

a = np.zeros(( n,n ))
for i in range(0, a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite um elemento:')
        
if quadradomagico(a):
    print 'S'
else:
    print 'N'
        

        
