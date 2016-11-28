# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,i]
    return soma

def somadiagonal2(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma+=a[i,a.shape[0]-i-1]
    return soma

def somalinhas(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma+=a[i,j]
        s.append(soma)
    return s
    
def somacolunas(a):
    s=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma+=a[i,j]
        s.append(soma)
    return s

def quadradomagico(a):
    
    sd1=somadiagonal1(a)
    sd2=somadiagonal2(a)
    sl=somalinhas(a)
    sc=somacolunas(a)
    
    cont=0
    for i in range(0,len(sl),1):
        if sd1==sd2==sl[i]==sc[i]:
            cont+=1
    
    if cont==len(sl):
        return True
    else:
        return False
    
n=input('digite a matriz:')
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]=input('digite o elemento:')
if quadradomagico(a):
    print('S')
else:
    print('N')
        
        
            
            
