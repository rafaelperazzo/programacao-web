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
    peso=(somaL+ somaC) 
    return peso
    
d=input('Digite a dimensão: ')
l=input('Digite a linha da posição : ')
c=input('Digite a coluna da posição: ')
xadrez=np.zeros((d,d))
for i in range (0,xadrez.shape[0],1):
    for j in range(0,xadrez.shape[1],1):
        xadrez[i,j]=input('Digite um valor: ')
        

print(pesoxadrez(xadrez,l,c))

