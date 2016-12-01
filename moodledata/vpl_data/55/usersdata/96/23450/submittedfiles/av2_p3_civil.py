# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def somalinha(a):
    soma = 0
    for i in range(0,n,1):
        soma = soma + a[i,y]
    return soma

def somacoluna(a):
    soma = 0
    for j in range(0,n,1):
        soma = soma + a[x,j]
    return soma

def peso(a):
    soma = (somalinha(a) + somacoluna(a)) - (2*(a[x,y]))
    return soma

n = input('Digite a dimensão da matriz:')
x = input('Digite a posição de x:')
y = input('Digite a posição de y:')
a = np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite um valor de a:')

print (peso(a))

