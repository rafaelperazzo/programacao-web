# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas = ínput('digite o número de linha: ')
colunas = ínput('digite o número de colunas: ')
a = np.zeros( (linhas,colunas) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('digite um elemento: ')
print a        



