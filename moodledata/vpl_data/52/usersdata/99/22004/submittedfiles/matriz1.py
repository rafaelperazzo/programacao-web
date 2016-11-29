# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#Funções
def menorcoluna(matriz):
    








#P.Principal
linhas=input('Digite a quantidade de linhas de a:')
colunas=input('Digite a quantidade de colunas de a:')

a=np.zeros( (linhas,colunas) )

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento para a matriz a:')
        
print 