# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
import numpy as np

def misterio(a):
    b=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            b.append(a[j,i])
    return b
    
n=input('N:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Elem:')
    
print a

print misterio(a)
        
        
        
        
        
