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
    b=[]
    for i in range(0,a.shape[0],1):
        s=0
        for j in range(0,a.shape[1],1):
            s=s+a[i,j]
        b.append(s)
    return b    
def somac(a):
    b=[]
    for j in range(0,a.shape[1],1):
        s=0
        for i in range(0,a.shape[0],1):
            s=s+a[i,j]
        b.append(s)
    return b        
def quadmag(a):
    sd1=somap(a)
    sd2=somas(a)
    sl=somal(a)
    sc=somac(a)
    c=0
    for i in range(0,len(sl),1):
        if sd1==sd2==sl[i]==sc[i]:
            c=c+1
    if c==len(sl):
        return True
    else:
        return False
n=input('digite o valor de n:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento:')
if quadmag(a):
    print('S')
else:
    print('N')