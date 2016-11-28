# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_diagonal(a):
    soma = 0
    for i in range (0,a.shape[0],1):
        soma = soma + a[i,i]
    return soma
def soma_diagonal_2 (a):
    soma = 0
    for i in range (0,a.shape[0],1):
        soma = soma + a[i,a.shape[0]-i-1]
    return soma    

n = input('digite a quantidade de elementos da matriz: ')
a = np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('digite os elementos de a: ')
        
print soma_diagonal_2(a)