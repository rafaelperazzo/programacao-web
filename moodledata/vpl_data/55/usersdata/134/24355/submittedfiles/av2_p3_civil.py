# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def pesolin(a,x):
    p = 0
    for i in range(0,a.shape[1],1):
        p = p + a[x,i]
    return p

def pesocol(a,y):
    p = 0
    for i in range(0,a.shape[0],1):
        p = p + a[i,y]
    return p
        
   
n = input('Digite a dimensão da matriz:')
x = input('Indice da linha:')
y = input('Indice da coluna:')
a = np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] =  input('Digite um elemento para a:')
        
b = pesolin(a,x)
c = pesocol(a,y)
d = (b + c) - 2*(a[x,y])
    
print d

    
