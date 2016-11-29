# -*- coding: utf-8 -*-
from __future__ import division
import numb as np

def diagonalp(a):
    s = 0
    for i in range(0, a.shape[0], 1):
        s = s + a[i,i]
    return s
    
    
def diagonal(a):
    s = 0
    for i in range (0, a.shape[0],1):
        s = s + a[i,a.shape[0]-1-i]
    return s
    
    
def somalinha(a):
    c = []
    for i in range(0, a.shape[0], 1):
        soma = 0
        for j in range(0, a.shape[0], 1):
            soma = soma
        
        
