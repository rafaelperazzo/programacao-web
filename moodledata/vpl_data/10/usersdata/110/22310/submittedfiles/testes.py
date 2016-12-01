# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def simetrica(a):
    colunaC=a.shape[0]//2
    cont=0
    for i in range(0,a.shape[0],1):
        b=a.shappe[0]-1
        for j in range(0,colunaC,1):
            if a[i,j]!=a[i,b]:
                cont=cont+1
            b=b-1
    if cont==0:
        return True
    else:
        return False
linhas=input('Digite linhas: ')
c=input('Digite colunas :' )
a=np.zeros((linhas,c))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite valor: ')
if simetrica(a):
    print('s')
else :
    print('n')