# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_linha(o):
    
    for i in range (0,o.shape[0],1):
        for j in range (0,o.shape[1],1):
            if o[i,j]==1:
                return menorl
            
def menor_coluna(o):
    
    for j in range(0,o.shape[1],1):
        for i in range(0,o.shape[0],1):
            if o[i,j]==1:
                return menorc
                
def maior_linha(o):
    maiorl=0
    for i in range(0,o.shape[0],1):
        for j in range(0,o.shape[1],1):
            if o[i,j]==1:
                maiorl=i
            
    return maiorl
    
def maior_coluna(o):
    maiorc=0
    for j in range(0,o.shape[1],1):
        for i in range(0,o.shape[0],1):
            if o[i,j]==1:
                maiorc=j
            
    return maiorc
                

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a qunatidade de colunas:')
a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento')

x=maior_linha(o)
y=maior_coluna(o)
z=menor_linha(o)
w=menor_coluna(o)
print (a[x:z+1,y:w+1])

        