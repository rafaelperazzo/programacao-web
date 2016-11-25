# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def ce(a):
    colesq=a.shape[0]-1
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            if a[i,j]==1:
                if j<=colesq:
                    colesq=j
    return colesq

def colunaD(a):
    coldir=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if j>=coldir:
                    coldir=j
    return coldir

def linhaC(a):
    linhaCima=a.shape[1]-1
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i<=linhaCima:
                    linhaCima=i
    return linhaCima
    
def lib(a):
    lb=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i>=lb:
                    lb=i
    return lb

linhas=input('número de linhas: ')
colunas=input('número de colunas: ')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elementos: ')

x=linhaC(a)
y=lib(a)+1
z=ce(a)
w=colunaD(a)+1

print (a[x:y,z:w])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    