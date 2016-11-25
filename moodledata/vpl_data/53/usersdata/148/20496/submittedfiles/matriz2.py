# -*- coding: utf-8 -*-
from __future__ import division

linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=ap.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento')


