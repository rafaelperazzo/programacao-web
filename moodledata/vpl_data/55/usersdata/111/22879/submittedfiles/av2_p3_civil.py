# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a,x,y):
    soma=0
    c=x-1
    d=y-1
    
    for i in range(c,a.shape[0]+1,1):
        for j in range(d,a.shape[1]+1,1):
            soma=soma+a[i,j]
    return soma-a[c,d]
    
n=input('Digite a dimensão da matriz: ')
a=np.zeros((n,n))

for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('Digite os elementos da matriz: ')
        
x=input('Digite o valor da posição x: ')
y=input('Digite o valor da posição y: ')

matriz=a[i,j]
resultado=peso(a,x,y) 
print matriz
print resultado
        
        






