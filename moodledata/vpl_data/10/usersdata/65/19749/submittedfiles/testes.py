# -*- coding: utf-8 -*-
from __future__ import division


def transposta(a):
    c=np.zeros((a.shape[1],a.shape[0]))
    
    for i in range(0,c.shape[1],1):
        for j in range(0,shape[0],1):
            c[i,j]=a[j,i]
    
    return c
    
#COMECE AQUI ABAIXO
import numpy as np


linhas=input('Digite as linhas : ')
colunas=input('Digite as colunas: ')

a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite os elementos de a: ')

print transposta(a)
