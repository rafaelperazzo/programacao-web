# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input ('insira a quantidade de linhas;') 
m = input ('insira a quantidade de culunas:') 

a=np.zeros ((n,m))
b=np.zeros ((n,m))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('insira um valor para a matriz:') 
        
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            b=[i:,:]
            break 

for k in range (0,a.shape[0],1):
    for l in range (0,a.shape[1],1):
        if a[k,l]==1:
            b=[i:k+1,:]
            
            
for o in range (0,a.shape[0],1):
    for p in range (0,a.shape[1],1):
        if a[o,p]==1:
            b=[i:k+1,p:]
            break 
        
for q in range (0,a.shape[0],1):
    for r in range (0,a.shape[1],1):
        if a[q,r]==1:
            b=[i:k+1,p:r]
            
            
            
print (b)
            
            