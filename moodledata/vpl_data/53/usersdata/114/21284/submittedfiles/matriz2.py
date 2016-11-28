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
def soma_linhas (a):
    s = []
    for i in range (0,a.shape[0],1):
        soma = 0
        for j in range (0,a.shape[1],1):
            soma = soma + a[i,j]
        s.append (soma)
    return s 
def soma_colunas (a):
    s = []
    for j in range (0,a.shape[1],1):
        soma = 0
        for i in range (0,a.shape[0],1):
            soma = soma + a[i,j]
        s.append (soma)
    return s  
def matriz_magica (a):
    sd1 = soma_diagonal (a)
    sd2 = soma_diagonal_2 (a)
    somaL = soma_linhas (a)
    somaC = soma_colunas (a)
    
    cont = 0
    for i in range (0,len(somaL),1):
        if sd1 == sd2 == somaL[i] == somaC[i]:
            cont = cont + 1
    if cont == len(somaL):
        return True
    else:
        return False

n = input('digite a quantidade de elementos da matriz: ')
a = np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('digite os elementos de a: ')
        
if matriz_magica (a):
    print ('S')
else:
    print ('N')