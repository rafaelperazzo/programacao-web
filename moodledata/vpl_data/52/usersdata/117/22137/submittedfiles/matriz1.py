# -*- coding: utf-8 -*-
from __future__ import division

def menorcoluna(a):
    for j in range (0,shape[1],1):
        for i in range (0, shape[0],1):
            if a[i,j]==1:
                ce=j
                break
    return ce
    
def menorcoluna(a):
    for j in range (0,shape[1],1):
        for i in range (0, shape[0],1):
            if a[i,j]==1:
                cd=j
    return cd
    
def menorlinha(a):
    for i in range (0,shape[0],1):
        for j in range (0, shape[1],1):
            if a[i,j]==1:
                lc=j
                break
    return lc
    
def menorlinha(a):
    for i in range (0,shape[0],1):
        for j in range (0, shape[1],1):
            if a[i,j]==1:
                lb=j
    return lb
    
