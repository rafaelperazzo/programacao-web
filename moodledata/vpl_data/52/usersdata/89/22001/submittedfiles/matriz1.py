# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def menorColuna(a):
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                return j
                
def maiorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
                
    return cd
    
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                return i
                
def maiorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lb=i
        
    return lb
    
n=input('digite o numero de linhas da matriz:')
m=input('digite o numero de colunas da matriz:')

a=np.zeros((n,m))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um elemento da matriz a:')
        
        
print(a[lc:lb+1,ce:cd+1])
