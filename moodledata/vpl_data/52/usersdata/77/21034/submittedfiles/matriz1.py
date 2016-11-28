# -*- coding: utf-8 -*-
from __future__ import division

def menorColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
                break
            
            
    return ce
    
def maiorrColuna(a):
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                cd=j
                
            
            
    return cd
    

def menorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                lc=i
                break
            
            
    return lc
    
def maiorLinha(a):
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                ld=i
                
            
            
    return ld
    

print(a[lc:lb+1,ce:cd+1])

    
    
    