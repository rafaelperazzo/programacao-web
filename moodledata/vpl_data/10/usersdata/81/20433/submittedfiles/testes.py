# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def transposta(a):
    linhas=a.shape[0]
    colunas=a.shape[1]
    c=np.zeros((linhas,colunas))
    for i in range(0,c.shape[0],1):
        for j in range(0,c.shape[1],1):
            c[i,j]=a[j,i]
    return c
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a:')
        
print transposta(a)

