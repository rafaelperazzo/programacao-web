# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input ('insira a quantidade de linhas:') 
m = input ('insira a quantidade de culunas:') 

a=np.zeros ((n,m))


cont1=0
cont2=0
cont3=0
cont4=0


for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input ('insira um valor para a matriz:') 
        
#primeira linha
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont1=i
            break 

#última linha
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            cont2=i
            
m=0           
#Primeira coluna 
for j in range (0,a.shape[1],1):
    for i in range (0,a.shape[0],1):
        if a[i,j]==1:
            if m==0:
                cont3=j
            if cont3<=j:
                cont3=j
        m=m+1

#Última coluna
for j in range (0,a.shape[1],1):
    for i in range (0,a.shape[0],1):
        if a[i,j]==1:
            if j>=cont4:
                cont4=j
            
print a[cont1:(cont2+1),cont3:(cont4+1)]
            
            