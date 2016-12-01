# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
n=input('digite a dimensão da matriz:')
x=input('digite o valor da linha:')
y=input('digite o valor da coluna:')

linhas=n
colunas=n
l=np.zeros((linhas,colunas))

for i in range(0,l.shape[0],1):
    for j in range(0,l.shape[1],1):
        l[i,j]=input('digite um elemento:')

