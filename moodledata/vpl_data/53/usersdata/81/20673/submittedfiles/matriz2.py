# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somad(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somad2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
def somal(a):
    t=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
    
def somac(a):
    t=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
        
