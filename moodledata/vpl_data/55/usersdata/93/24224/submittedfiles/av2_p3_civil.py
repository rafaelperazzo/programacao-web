# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('n: ')
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('elemento da matriz: ')
x=input('indice da linha: ')
y=input('indice da coluna: ')
soma=-2*a[x,y]
for j in range(0,a.shape[1],1):
    soma=soma+a[x,j]
for i in range(0,a.shape[0],1):
    soma=soma+a[i,y]
print soma