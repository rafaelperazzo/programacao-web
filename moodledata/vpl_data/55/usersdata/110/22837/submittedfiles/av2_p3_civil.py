# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def pesoxadrez(a,l,c):
    somaL=0
    somaC=0
    for j in range(0,a.shape[1],1):
        somaL=somaL+a[l,j]
    for i in range(0,a.shape[0],1):
        somaC=somaC+a[i,c]
    peso=somaL+ somaC -(2*a[l,c])
    return somaL
    
d=input('Digite a dimensão: ')
i=input('Digite a linha da posição : ')
j=input('Digite a coluna da posição: ')
xadrez=np.zeros((d,d))
for i in range (0,xadrez.shape[0],1):
    for j in range(0,xadrez.shape[1],1):
        xadrez[i,j]=input('Digite um valor: ')
        
print(pesoxadrez(xadrez,i,j))

