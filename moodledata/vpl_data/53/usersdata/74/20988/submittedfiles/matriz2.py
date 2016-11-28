# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def matrixm(a):
    soma = 0
    soma1 = 0
    l = a.shape[0]
    c = a.shape[1]
    i = 0
    j = 0
    k = 0
    cont = 0
    
    while (l-1)>=k:
        soma = soma+a[k,0]
        k = k+1
        
    
    while (c-1)>=j:
        while (l-1)>=i:
            soma1 = soma1+a[i,j]
            i = i+1
        if soma == soma1:
            cont = cont+1
        j = j+1
    
    i = 0
    j = 0
    soma1 = 0
    
    while (l-1)>=i:
        while (c-1)>=j:
            soma1 = soma1+a[i,j]
            j = j+1
        if soma == soma1:
            cont = cont+1
        i = i+1
        
    if cont == (l+c):
        return True
    else:
        return False
    
n = input('Número de linhas e colunas da matriz: ')

b = np.zeros((n,n))
x = 0
y = 0

while (n-1)>=x:
    while (n-1)>=y:
        b[x,y] = input('Digite os elementos: ')
        y = y+1
    x = x+1
    y = 0

print b
matrixm(b)
