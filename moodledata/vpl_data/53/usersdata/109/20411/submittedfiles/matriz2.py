# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def SomaDiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def SomaDiagonal2(a):
    
    


n=input('Digite a dimensao da matriz quadrada:')
linhas=n
colunas=n
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

