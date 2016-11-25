# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def linhainf(a):
    l1=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                l1=i
    return l1
def linhainf(a):
    l2=0
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                l2=i
                break
        break
    return l2
def colunadir(a):    
    c1=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                c1=j
                break
        break
    return c1
def colunaesq(a):
    c2=0
    for j in range(a.shape[1]-1,-1,-1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                c2=j
                break
        break
    return (c2)
n=input('n: ')
m=input('m: ')
a=np.zeros((n,m))
for i in range(0,n,1):
    for j in range(0,m,1):
        a[i,j]=input('elemento da matriz: ')
print(linhasup(a))
print a