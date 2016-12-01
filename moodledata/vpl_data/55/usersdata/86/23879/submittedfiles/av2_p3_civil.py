# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n= input('n:')
x=input('digite indice da linha:')
y=input('digite indice da coluna:')
b= np.zeros((n,n))
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=input('b:')
soma=0
for i in range(0,b.shape[0],1):
    soma=soma+b[i,y]
for i in range(0,b.shape[1],1):
    soma=soma+b[x,i]
soma=soma-2*b[x,y]
print(soma)
