# -*- coding: utf-8 -*-
from __future__ import division

def somalinhas(a):
    somaL=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+ a[i,j]
        somaL.append(soma)
    return somaL
linhas=input('Digite linhas: ')
c=input('Digite colunas :' )
a=np.zeros((linhas,c))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite valor: ')
print( somalinhas(a))