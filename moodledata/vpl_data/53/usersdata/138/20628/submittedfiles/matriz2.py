# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 
def somaL(a):
    l=[]
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
            a.insert(0,a[i,j])
    return l
    
def somaC(a):
    l=[]
    soma=0
    for j in range(0.a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            a.insert(0,a[i,j])
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
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

