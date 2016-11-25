# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#FUNÇÃO DE TESTE
def linhadebaixo(a):
    lb=0
    for j in range(a.shape[0],1,1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                lb=i
                break
    return lb
#PROGRAMA PRINCIPAL
linhas=input('Digite uma quantidade de linhas:')
colunas=input('Digite uma quantidade de colunas:')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')

print a[:,:]

print a[0:2,0:2]