# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinhas (a):
    s=[]
    for i in range (0,a.shape[i],1):
        soma=0
        for j in range (0,a.shape[j],1):
            soma=soma+a[i,j]
            s.append(soma)
    return s
    
n=input('Digite o valor de n:')
linhas=n
colunas=n
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,shape[1],1):
        a[i,j]=input('Digite um valor para a matriz: ')
        
print somalinhas(a)
