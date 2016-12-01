# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Digite o valor de n: ')
x=input('Digite o valor de x: ')
y=input('Digite o valor de y: ')
linha=n
coluna=linha

a=np.zeros((linha,coluna))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento para a matriz A: ')

somalinha=0        
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i==x:
            somalinha=somalinha+a[i,j]
            
somacoluna=0
for j in range(0,a.shape[0],1):
    for i in range (0,a.shape[1],1):
        if j==y:
            somacoluna=somacoluna+a[i,j]
            
somatotal=somalinha+somacoluna
somatotal=somatotal-(2*a[i,j])
print a