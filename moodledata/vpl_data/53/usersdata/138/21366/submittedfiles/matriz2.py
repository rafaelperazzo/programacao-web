# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
def somaL(a):
    l=[]
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
            a.insert(0,a[i,j])
    return l
    
def somaC(a):
    l=[]
    soma=0
    for j in range(0.a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            a.insert(0,a[i,j])
    return l
    
def diagonalP(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return soma

def diagonalS(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if (i+j)==a.shape[0]-1:
                soma=soma+a[i,j]
    return soma
    
def quadradomagico(a):
    sc=somaC(a)
    sl=somaL(a)
    dp=diagonalP(a)
    ds=diagonalS(a)
    for i in range(0,len(sc),1):
        if sc[i]==sl[i] and dp==ds and sc[i]==dp :
            return True 
        else:
            return False

n=input('n:')
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('digite um valor:')
if quadradomagico(a):
    print ('S')
else:
    print ('N')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

