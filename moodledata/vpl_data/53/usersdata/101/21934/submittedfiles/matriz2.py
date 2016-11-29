# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagona_1(a):
    soma = 0
    for i in range (a, a.shape[0], 1):
        soma = soma + a[i,j]
    return soma

def soma_diagona_2(a):
    soma = 0
    for i in range (a, a.shape[0], 1):
        soma = soma + a[i, a.shape[0] - i -1]
    return soma
    
def soma_linha(a):
    b = []
    for i in range (0, a.shape[0], 1):
        soma = 0
        for j in range (0, a.shape[1], 1):
            soma = soma + a[i,j]
        b.append(soma)
    return b
    
def soma_coluna(a):
    c = []
    for i in range (0, a.shape[0], 1):
        c.append(sum(a[i, :]))
    return c
    
def quadrado_magico(a):
    x = soma_diagona_1(a)
    y = soma_diagona_2(a)
    z = soma_linha(a)
    t = soma_coluna(a)
    
    cont = 0
    
    for i in range (0, len(z), 1):
        if x == y == z[i] == t[i]:
            cont = cont + 1
    if cont == len(z):
        return True
    else:
        return False
        

n = input(' Digite um valor para n: ')
a = np.zeros((n,n))

for i in range (0, a.shape[0], 1):
    for j in range (0, a.shape[1], 1):
        a[i,j] = input('Digite qualquer elemento: ')

if quadrado_magico(a):
    print ('S')
else:
    print ('N')