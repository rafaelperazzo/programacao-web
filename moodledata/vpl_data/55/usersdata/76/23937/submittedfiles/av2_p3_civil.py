# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinhas(a,x):
    soma = 0
    for j in range(0,a.shape[1],1):
        soma = soma + a[n,j]
    return soma


def somacolunas(a,y):
    soma = 0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,y]
    return soma
    

def somatotal(a,x,y):
    soma = 0
    soma = somalinhas(a,x) + somacolunas(a,y) - (2*a[x,y])
    return soma
    
n = input('Digite o valor de n:')
x = input('Digite a linha:')
y = input('Digite a coluna:')
a = np.zeros ((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite os elementos da matriz:')
        
smt = somatotal(a,x,y)
print smT