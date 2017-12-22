# -*- coding: utf-8 -*-
import numpy as np

n=int(input('digite: '))

m=n

a=np.zeros((n,m))

for i in range(0,n,1):
    for j in range(0,m,1):
        a[i,j]= float(input('digite: '))
        
soma=0
cont=o

for i in range(0,n,1):
    for j in range(0,m,1):
        soma=soma+a[i,j]
    if soma-a[i,i]<a[i,i]:
        cont=cont+1
    soma=0
if cont==n:
    print('SIM')
else:
    print('NAO')
