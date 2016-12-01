# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Digite o valor de n: ')
x=input('Digite o valor de x: ')
y=input('Digite o valor de y: ')
linha=n
coluna=n

a=np.zeros((linha,coluna))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento para a matriz A: ')

somap=0        
for i in range (0,a.shape[1],1):
    for j in range (0,a.shape[0],1):
        if i==x:
            somap=somap+a[i,j]
            
somas=0
for j in range(0,a.shape[1],1):
    for i in range (0,a.shape[0],1):
        if j==y:
            somas=somas+a[i,j]
            
somat=somap+somas
somat=somat-(2*a[x,y])

print a
