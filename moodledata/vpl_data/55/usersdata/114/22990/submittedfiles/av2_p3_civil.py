# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha (a,i):
    soma_linha = 0
    for j in range (0,a.shape[1],1):
        soma_linha = soma_linha + a[i,j]
    return soma_linha
    
def somaColuna (a,j):
    soma_coluna = 0
    for i in range (o,a.shape[0],1):
        soma_coluna = soma_coluna + a[i,j]
    return soma_coluna
    
def peso (a,i,j):
    soma_peso = somaLinha(a,i) + somaColuna(a,j) - (2 * a[i,j] )
    return soma_peso

n = input('digite a dimensão da matriz: ')

x = input('digite o índice i: ')
y = input('digite o índice j: ')

a = np.zeros ((n,n))
for i in range (0,shape[o],1):
    for j in range (0,shape[j],1):
        a[i,j] = input('digite o elemento: ')
pesox = peso (a,x,y)        
print ('%d' %pesox)      