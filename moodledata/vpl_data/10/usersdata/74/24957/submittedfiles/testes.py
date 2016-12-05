# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somal(b):
    soma = 0
    i = 0
    j = 0
    v = []
    n = b.shape[0]-1
    m = b.shape[1]-1
    while n>=i:
        while m>=j:
            soma = soma + b[i,j]
            j = j+1
        v[i] = soma
        i = i+1
        j = 0
    
def somac(c):
    soma = 0
    i = 0
    j = 0
    v = []
    m = c.shape[0]-1
    n = c.shape[1]-1
    while n>=i:
        while m>=j:
            soma = soma + c[j,i]
            j = j+1
        v[i] = soma
        i = i+1
        j = 0


    
x = input('Número de linhas da matriz quadrada: ')

a = np.zeros((x,x))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite o valor: ')




