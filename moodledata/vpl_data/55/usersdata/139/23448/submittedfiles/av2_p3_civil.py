# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('digite o tamanho do tabuleiro:')
c=input('digite a casa que deseja saber do peso:')
soma=0
a=np.zeros((n,n))
x=c-1

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o valor da casa do tabuleiro:')
for k in range(0,c,1):
    soma=soma+a[k,x]
for l in range(0,c,1):
    soma=soma+a[x,k]
soma=soma-2*a[x,x]
print soma
