# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o elementos:')
        
def primeiraLinha(a):
    for i in range (0,len(a),1):
        if i in a[i]:
            return a[i]
print primeiraLinha(a)