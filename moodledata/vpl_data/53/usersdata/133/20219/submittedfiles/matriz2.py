# -*- coding: utf-8 -*-
from __future__ import division

def diagonalp(a):
    s = 0
    for i in range(0, a.shape[0], 1):
        s = s + a[i,i]
return s


def diagonals(a):
    s = 0
    for i in range(0, a.shape[0],1):
        s = s + a[i,a.shape[0]-1-i]
return s


def samalinha(a):
    s = []
    for i in range(0, a.shape[0], 1):
        s[i] = 0
    for i in range(0, a.shape[0], 1):
        for j in range(0, a.shape[0], 1):
            s[i]= s[i] + a[i,j]
return s


def somacoluna(a):
    s = []
    for i in range(0, a.shape[0], 1):
        s[i] =0
    for i in range
    
    
    
    
    
    
    