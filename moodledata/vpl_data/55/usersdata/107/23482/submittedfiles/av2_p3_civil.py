# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso_posicao(M,n,p):
    cont1=0
    cont2=0
    for i in range(0,M.shape[1],1):
        cont1=cont1+M[n,i]
    for i in range(0,M.shape[1],1):
        cont2=cont2+M[i,p]
    cont=cont1+cont2-2*M[n,p]
    return cont
    
m=input('digite a dimensao da matriz:')
d=input('digite o indice da linha:')
r=input('digite o indice da coluna:')
M=np.zeros((m,m))
for i in range(0,m,1):
    for j in range (0,m,1):
        M[i,j]=input('digite o elemento da matriz:')
cont1=peso_posicao(M,d,r)
print ('%d' %cont1)


    
