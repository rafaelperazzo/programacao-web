# -*- coding: utf-8 -*-
from __future__ import division

def menorcoluna(a):
    ce=0
    for j in range(0,a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                ce=i
                break
    return ce

def maiorcoluna(a):
    cd=0
    for j in range(0,a.shape[1],1):
        for i in range(0, a.shape[0],1):
            if a[i,j]==1:
                cd=i
    return cd
    
def menorlinha(a):
    lc=0
    for i in range(0,a.shape[0],1):
        for j in range(0, a.shape[1],1):
            if a[i,j]==1:
                lc=i
                break
    return lc
    
def maiorlinha(a):
    lb=0
    for i in range(0,a.shape[0],1):
        for j in range(0, a.shape[1],1):
            if a[i,j]==1:
                lb=i
    return lb

a=[]    
m=input('digite o numero de colunas:')
n=input('digite o numero de linhas:')
for i in range(0,n,1):
    for i in range(0,m,1):
        a.append(input('digite o elemento:'))
