# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def diagonals(a):
    s = 0
    for i in range(0, a.shape[0], 1):
        s = s + a[i,i]
    return s
    
    
def diagonals(a):
    s = 0
    for i in range(0, a.shape[0],1):
        s = s + a[i,a.shape[0]-1-i]
    return s
    
    
def somalinha(a):
    c=[]
    for i in range(0,a.shape[0], 1):
        soma = 0 
        for j in range(0, a.shape[0], 1):
            soma = soma a[i,j]
        c.append(soma)
    return c
    
def somacoluna(a):
    c=[]
    for j in range(0, a.shape[0], 1):
        soma = 0
        for i in range(0, a.shape[0], 1):
            soma = soma + a[i,j]
        c.append(soma)
    return c
    
def verifica(a):
    b=diagonalp(a)
    c=diagonals(a)
    d=somalinha(a)
    e=somacoluna(a)
    
    for i in range