# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n= input('n')
b= np.zeros((n,n))
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        a[i,j]=input('a')
soma=0
for i in range(0,b.shape[0],1):
    soma=soma+b[i,y]
for i in range(0,b.shape[1],1):
    soma=soma+b[x,i]
print(soma)
