# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somalinha(a,b):
    z=0
    for j in range(0,a.shape[1],1):
        z=z+a[b,j]
    return z
        
def somacoluna(a,c):
    z=0
    for i in range(0,a.shape[0],1):
        z=z+a[i,c]
    return z

def somatotal(a,b,c):
    soma=somalinha(a,b)+somacoluna(a,c)-(2*a[b,c])
    return soma

n=input('digite o valor de n:')
x=input('digite o valor de x:')
y=input('digite o valor de y:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite os elementos:')

print('%d'%(somatotal(a,x,y)))
    
