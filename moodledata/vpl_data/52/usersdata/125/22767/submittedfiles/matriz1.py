# -*- coding: utf-8 -*-
from __future__ import division

def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                CE=j
                break
    return CE
    
def maiorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                CD=j
                
    return CD
    
def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                LC=i
                break
    return LC
    
def maiorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                LB=i
                
    return LB
    
    
def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a,shape[0],1):
            if a[i,j]==1:
                return j
    
def maiorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a,shape[0],1):
            if a[i,j]==1:
                CD=j
    return CD
    
print("a[lc:lb+1,ce:cd+1]")
    
    
    
    