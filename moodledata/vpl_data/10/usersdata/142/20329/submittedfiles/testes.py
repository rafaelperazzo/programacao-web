# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas=input('Digite uma quantidade de linhas:')
colunas=input('Digite uma quantidade de colunas:')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')

print a[:,:]
print a[0:3,0:3]