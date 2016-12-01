# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha(a,x):
    soma = 0
    for j in range(0,a.shape[1],1):
        soma = soma + a[n,j]
    return soma

def somaColuna(a,y):
    soma = 0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,y]
    return soma
    
def somaTotal(a,x,y):
    soma = 0
    soma = somaLinha(a,x) + somacoLuna(a,y) - (2*a[x,y])
    return soma
    
n = input('Digite o valor de n:')
x = input('Digite a linha:')
y = input('Digite a coluna:')
a = np.zeros ((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite os elementos da matriz:')
        
smT = somaTotal(a,x,y)
print smT