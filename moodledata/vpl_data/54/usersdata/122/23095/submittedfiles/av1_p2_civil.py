# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinhas (a):
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
    return soma
    
n=input('Digite o valor de n:')

#idp=indice de posição
idp=[x,y]

linhas=n
colunas=n
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz: ')
        

