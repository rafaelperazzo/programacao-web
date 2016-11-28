# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input ('insira a quantidade de linhas;') 
m = input ('insira a quantidade de culunas:') 

a=np.zeros ((n,m))


cont=0
cont2=0
cont3=0
con4=0


for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('insira um valor para a matriz:') 
        
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont=i
            break 

for k in range (0,a.shape[0],1):
    for l in range (0,a.shape[1],1):
        if a[k,l]==1:
            cont2=k
            
            
for o in range (0,a.shape[0],1):
    for p in range (0,a.shape[1],1):
        if a[o,p]==1:
            cont3=p
            break 
        
for q in range (0,a.shape[0],1):
    for r in range (0,a.shape[1],1):
        if a[q,r]==1:
            cont4=r
            
            
            
print a[cont:(cont2+1),cont3:(cont4+1)]
            
            