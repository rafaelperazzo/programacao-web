# -*- coding: utf-8 -*-
from __future__ import division

def somaLinhas(a):
    s=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma = soma+a[i,j]
        s.append (soma)
    return s
    
def somaColunas(a):
    s=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma = soma+a[i,j]
        s.append (soma)
    return s
    
def diagonalSecundaria(a):
    soma = 0
    for i in range (0,a.shape[0],1):
        soma = soma+a[i,a.shape[0]-i-1]
    return soma
        
def somaDiagonal(a):
    soma = 0
    for i in range (0,a.shape[0],1):
        soma = soma+a[i,i]
    return soma
    
a=[]
n = input ('Digite o valor de n:')

for i in range (0,n,1):
    a.append (input('Digite o valor de a:'))
