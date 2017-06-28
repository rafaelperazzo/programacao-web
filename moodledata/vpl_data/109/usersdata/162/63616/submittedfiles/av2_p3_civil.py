# -*- coding: utf-8 -*-
import numpy as np
n=int(input('n:'))
a=n.zeros((n,n))
x=int(input('Digite o índice da posição linha:'))
y=int(input('Digite o indice da posição coluna:'))
somaLinha=0
somaColuna=0
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite peso:'))
for i in range(0,a.shape[0],1):
    for j in range(o,a.shape[1],1):
        if i==x:
            somaLinha=somaLinha+a[i,j]
        if j==y:
            somaColuna=somaColuna+a[i,j]
peso=somaLinha+somaColuna-(2*a[i,j])
print(peso)
