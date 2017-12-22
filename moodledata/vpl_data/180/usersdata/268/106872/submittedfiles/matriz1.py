# -*- coding: utf-8 -*-
import numpy as np

linhas= int(input('Digite linhas :' ))
colunas:int(input('Digite colunas: '))

a= np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = int(input('Digite o elemento:'))

print(a)