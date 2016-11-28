# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o elemento:')

def colunaE(a):
    ce=0
    for i in range(0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                if j>=ce:
                    ce=j
    return ce
def colunaD(a):
    cd=a.shape[0]-1
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                if j<=cd:
                    cd=j
    return cd
def linhaC(a):
    lc=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i>=lc:
                    lc=i
    return lc
def linhab(a):
    lb=a.shape[1]-1
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if i<=lb:
                    lb=i
    return lb
    
print (a[linhab(a):linhaC(a)+1,colunaD(a):colunaE(a)+1])


                