# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite a dimensão da matriz:'))
ind=float(input('digite o indice da posição:'))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('digite o elemento da matriz:'))
x=ind//10
y=ind%10
i=x
soma=0
for j in range (0,a.shape[1],1):
    soma=soma+a[i,j]
j=y    
for i in range (0,a.shape[0],1):
    soma=soma+a[i,j]
soma=soma-(a[x,y]*2)
print(soma)