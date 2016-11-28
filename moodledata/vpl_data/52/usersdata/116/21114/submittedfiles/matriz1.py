# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input ('insira a quantidade de linhas:') 
m = input ('insira a quantidade de culunas:') 

a=np.zeros ((n,m))


cont1=0
cont2=0
cont3=0
con4=0


for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('insira um valor para a matriz:') 
        
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont1=i
            break 

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont2=i
            
            
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont3=j
            break 
        
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont4=j+1
            
            
            
print a[cont1:(cont2+1),cont3:(cont4+1)]
            
            