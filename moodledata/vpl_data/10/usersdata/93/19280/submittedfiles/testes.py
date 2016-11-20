# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE9 AQUI ABAIXO
def soma(a,b):
    c=np.zeros((a.shape[0],a.shape[1]))
    for i in range(0,c.shape[0],1):
        for j in range(0,c.shape[1],1):
            c[i,j]=a[i,j]+b[i,j]
    return c
def transposta(a):
    c=np.zeros((a.shape[1]),a.shape[0])
    for i in range(0,c.shape[0],1):
        for j in range(0,c.shape[1],1):
            c[i,j]=a[j,i]
    return c
linhas=input('linhas')
colunas=input('colunas')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elemento de a')
print(transposta(a))