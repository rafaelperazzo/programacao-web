# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite o número de elementos: '))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor: '))

linha=0
coluna=0
x=0
while(o<n):
    for k in range (0,a.shape[0],1):
        for l in range (0,a.shape[1],1):
            linha=linha+a[0,l]
            coluna=coluna+

