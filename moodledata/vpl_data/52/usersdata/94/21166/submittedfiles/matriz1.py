# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menor_linha(a):
    
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                return menorl
            
def menor_coluna(b):
    
    for j in range(0,b.shape[1],1):
        for i in range(0,b.shape[0],1):
            if b[i,j]==1:
                return menorc
                
def maior_linha(c):
    maiorl=0
    for i in range(0,c.shape[0],1):
        for j in range(0,c.shape[1],1):
            if c[i,j]==1:
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

x=maior_linha(a)
y=maior_coluna(a)
z=menor_linha(a)
w=menor_coluna(a)
print (a[z:x+1,w:y+1])

        