# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas=input('Digite o numero de linhas:')
colunas=input('Digite o número de colunas:')
matriz=np.zeros((linhas,colunas))
for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        matriz[i,j]=input('Digite um valor pra matriz:')
print matriz

    
