# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE9 AQUI ABAIXO
linhas=input('linhas')
colunas=input('colunas')
a=np.zeros((linhas,colunas))
b=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elemento de a')
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=input('elemento de b')
c=np.zeros((linhas,colunas))
for i in range(0,c.shape[0],1):
    for j in range(0,c.shape[1],1):
        c[i,j]=a[i,j]+b[i,j]
print c