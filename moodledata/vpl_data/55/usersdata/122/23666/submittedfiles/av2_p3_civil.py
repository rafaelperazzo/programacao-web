# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np


n=input('Digite o valor de n:')
linhas=n
colunas=n


a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz: ')

x=input('Digite i:')
y=input('Digite j:')
a[x,y]

print [x,y]