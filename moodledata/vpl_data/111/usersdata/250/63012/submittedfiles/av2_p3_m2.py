# -*- coding: utf-8 -*-
import numpy as np
def Slinhas(a):
    soma=0
    for l in range (0,a.shape[0],1):
        for c in range (0,a.shape[1],1):
            soma=soma+a[l,c]
        return(soma)
def Scolunas(a):
    soma=0
    for c in range (0,a.shape[1],1):
        for l in range (0,a.shape[0],1):
            soma=soma+a[l,c]
        return(soma)
def Slinhas(a):
    soma=0
    for l in range (0,a.shape[0],1):
        for c in range (0,a.shape[1],1):
            soma=soma+a[l,c]
        return(soma)
def Sdiagonal(a):
    soma=0
    for l in range (0,a.shape[0],1):
        for c in range (0,a.shape[1],1):
            if l==c:
                soma=soma+a[l,c]
    return(soma)
    
        

