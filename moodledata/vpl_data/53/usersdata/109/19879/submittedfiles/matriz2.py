# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Digite a dimensao da matriz quadrada:')

linhas=n
colunas=n

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

cont=0

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        cont=a[i,j]+cont
        if cont==cont2:
            cont3=1
        else:
            cont3=0
    cont2==cont
    