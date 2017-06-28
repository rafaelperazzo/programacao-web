# -*- coding: utf-8 -*-
import numpy as np
def r(a):
    soma=0
    soma1=0
    soma2=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,0]
        soma1=soma1+a[i,1]
        soma2=soma2+a[i,2]
    if soma==soma1:
        r=soma
    else:
        r=soma2
    return r
    
def linhaErrada(a,p):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j range(0,a.shape[1],1):
            soma=soma+a[i,j]
            b.append(soma)
    for i in range(0,len(b),1):
        if b[i]!=p:
            return i
            
def colunaErrada(a,v):
    c=[]
    for j in range(0,)
    

