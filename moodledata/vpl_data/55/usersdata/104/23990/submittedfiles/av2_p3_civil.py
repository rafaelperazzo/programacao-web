# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('Digite a dimensão:')
l=input('Digite o indice da linha:')
c=input('Digite o indice da coluna:')
z=np.zeros((n,n))
cont=0
for i in range(0,z.shape[0],1):
    for j in range(0,z.shape[1],1):
        z[i,j]=input('Digite um valor pra matriz:')

for i in range(0,z.shape[0],1):
    for j in range(0,z.shape[1],1):
        if i==l:
            cont=cont+z[i,j]
        elif j==c:
            cont=cont+z[i,j]
        elif i==j:
            cont=cont
print cont

