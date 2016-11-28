# -*- coding: utf-8 -*-
from __future__ import division
def somaDiagonal1(a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,i]
return soma
def somaDiagonal2(a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
return soma
def somaLinhas(a):
    s=0
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append
    return s
def somaColunas(a):
    z=0
    for j in range (0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        z.append
    return z
n=input('n:')
a=np.zeros((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]=input('digite um valor:')
if quadradomagico(a):
    print('s')
else:
    print ('n')
    
