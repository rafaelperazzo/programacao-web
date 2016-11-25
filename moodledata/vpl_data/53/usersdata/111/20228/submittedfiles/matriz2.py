# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def diagsec(a):
    x=a.shape[1]-1
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==x:
                soma=soma+a[i,j]
                x=x-1
    return soma
    
def diagprim(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    return soma
    
def somalinha(a):
    s=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s
    

    

            












