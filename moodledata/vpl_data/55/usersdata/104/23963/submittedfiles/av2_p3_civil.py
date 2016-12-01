# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('Digite a dimensão:')
l=input('Digite o indice da linha:')
c=input('Digite o indice da coluna:')
z=np.zeros((n,n))
soma=0
for i in range(0,z.shape[0],1):
    for j in range(0,z.shape[1],1):
        z[i,j]=input('Digite um valor pra matriz:')
print z

