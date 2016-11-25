# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def somap(a):
    s=0
    for i in range(0,a.shape[0],1):
        s=s+a[i,i]
    return s    
def somas(a):
    s=0
    i=0
    j=a.shape[0]-1
    while(i<a.shape[0]):
        s=s+a[i,j]
        i=i+1
        j=j-1
    return s  
def somal(a):
    a=[]
    for i in range(0,a.shape[0],1):
        s=0
        for j in range(0,a.shape[1],1):
            s=s+a[i,j]
        a.append(s)
    return a    
n=input('digite o valor de n:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento:')
print(somal(a))