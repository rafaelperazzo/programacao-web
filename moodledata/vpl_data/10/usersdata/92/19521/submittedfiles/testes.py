# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas= input('Digite o numero de linhas: ')
colunas= input('Digite o numero de colunas: ')

a= np.zeros((linhas, colunas))

for i in range(0, a.shape[0], 1):
    for j in range(0, a.shape[1], 1):
        a[i,j]= input('Digite um elemento: ')

print (a)