# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def somalinha(x,i,j):
    b=sum(x[i,:])
    c=b-(x[i,j])
    return c
def somacoluna(x,i,j):
    p=sum(x[:,j])
    r=p-(x[i,j])
    return r

linha=input ('Digite a quantidade de linhas da matriz:')
l=input('digite o indice da linha:')
c=input('digite o indice da coluna:')
a=np.zeros((linha,linha))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')
Pl=somalinha(a,l,c)
Pc=somacoluna(a,l,c)

print ('%d'%(Pc+Pl))