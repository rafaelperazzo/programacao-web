# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaM(m,l,c):
    soma1=0
    for i in range(0,m.shape[0],1):
        soma1=soma1+m[i,c]
    soma2=0
    for j in range(0,m.shape[1],1):
        soma2=soma2+m[l,j]
    soma=soma1+soma2-(2*(m[l,c]))

n=input('digite a ordem da matriz:')
l=input('digite a linha:')
c=input('digite a coluna:')
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=(input('digite um valor:'))

peso=somaM(a,l,c)
print ('peso')

