# -*- coding: utf-8 -*-

import numpy as np

m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))

a=np.zeros((m,n))

for i in range(0,m,1):
    for j in range(0,n,1):
        a[i,j]= float(input('Digite os elementos: '))
matriz= np.zeros((m,n))

l= m-1
c= m-1

for i in range(0,m,1):
    for i in range(0,n,1):
        matriz[l,c]=a[i,j]
        c=c-1
    c=n-1
    l=l-1
    
print(matriz)