# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('digite a dimensão da matriz:')
x=input('digite o valor de x:')
y=input('digite o valor de y:')

linhas=n
colunas=n
l=np.zeros((linhas,colunas))

for i in range(0,l.shape[0],1):
    for j in range(0,l.shape[1],1):
        l[i,j]=input('digite um elemento:')

soma1=0
for i in range(0,l.shape[0],1):
    for j in range(0,l.shape[1],1):
        if i==x:
            soma1=soma1+l[i,j]

soma2=0
for j in range(0,l.shape[1],1):
    for i in range(0,l.shape[0],1):
        if j==y:
            soma2=soma2+l[i,j]

somat=soma1 + soma2
somat=somat-(2*l[x,y])

print somat



