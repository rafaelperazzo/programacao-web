# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def pesoxadrez(a,l,c):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[l,j]
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,c]
    peso=soma-(2*a[l,c])
    return peso
d=input('Digite a dimensão: ')
i=input('Digite a linha da posição : ')
j=input('Digite a coluna da posição: ')
xadrez=np.zeros((d,d))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        xadrez[i,j]=input('Digite um valor: ')
        
print(pesoxadrez(xadrez,i,j))

