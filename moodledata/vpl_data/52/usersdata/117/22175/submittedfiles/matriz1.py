# -*- coding: utf-8 -*-
from __future__ import division

def menorcoluna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
    
def menorcoluna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return i
    
def menorlinha(a):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                lb=j
    return lb
    
n=input('Digite o número de linhas:')
m=input('Digite o número de colunas:')
import numpy as np
a=np.zeros ( (n , m) )

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

ce=menorcoluna(a)
lc=menorlinha(a)
print (a[lc:lb+1,ce:cd+1])
    
