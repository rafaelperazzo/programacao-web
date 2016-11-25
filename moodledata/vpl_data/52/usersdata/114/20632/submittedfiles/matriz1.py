# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def coluna_da_esquerda (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j] == 1:
                return j
def coluna_da_direita (a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j] == 1:
                cd = j
    return cd
def linha_de_cima (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j] == 1:
                return i    
def linha_de_baixo (a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j] == 1:
                lb = i
    return lb            

n = input('digite o número de linhas: ')
m = input('digite o número de colunas: ')
a = np.zeros( (n,m) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('digite um elemento: ')
        
ce = coluna_da_esquerda (a)
cd = coluna_da_direita (a)
lc = linha_de_cima (a)
lb = linha_de_baixo (a)
        
print ( a[lc:lb+1,ce:cd+1] )        



