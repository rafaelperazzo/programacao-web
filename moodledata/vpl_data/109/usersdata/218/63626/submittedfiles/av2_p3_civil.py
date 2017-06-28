# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite a dimensão da matriz:'))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('digite o elemento da matriz:'))
l=int(input('digite o indice da linha:'))
c=int(input('digite o indice da coluna:'))
i=l
for j in range (0,a.shape[1],1):
    soma=soma+a[i,j]
j=c
for i in range (0,a.shape[0],1):
    soma=soma+a[i,j]
valor=soma-(2*a[l,c])    
print(valor)