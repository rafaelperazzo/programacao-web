# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Funções
def somaDiagonalP(a):
    soma = 0
    for i in range(0,a.shape[1],1):
        soma = soma + a[i,i]
    return soma

def somaDiagonalS(a):
    soma = 0
    for i in range(0,a.shape[1],1):
        soma = soma + a[i,a.shape[1]-1-i]
    return soma

def somaLinhas(a):
    s = []
    for i in range(0,a.shape[1],1):
        s.append(sum(a[i,:]))
    return s

def somaColunas(a):
    s = []
    for i in range(0,a.shape[1],1):
        s.append(sum(a[:,i]))
    return s
    
def quadradoMagico(a):
    dp = somaDiagonalP(a)
    ds = somaDiagonalS(a)
    L = somaLinhas(a)
    C = somaLinhas(a)
    
    cont = 0
    for i in range(0,len(L),1):
        if dp == ds == L[i] == C[i]:
            cont = cont +1
            
    if cont == len(L):
        return True
    else:
        return False
        
#Programa Principal
n = input('Digite o número de linhas/colunas (n>2) :')
a = np.zeros((n,n))

for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j] = input('Digite um valor para a matriz:')
    
if quadradoMagico(a):
    print('S')
else:
    print('N')
