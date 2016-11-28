# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

def somaL(a):
    l=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
            l.append(soma)
    return l
    
def somaC(a):
    l=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            l.append(soma)
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
    cont=0
    for i in range(0,len(sl),1):
        if sp==ds==sc[i]==sl[i]:
            cont=cont+1
    if cont==len(sl):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

