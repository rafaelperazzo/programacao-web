# -*- coding: utf-8 -*-
import numpy as np
def slinhas(a):
    soma=0
    for i in range(0,a.shape[0],1):
        for l in range(0,a.shape[1],1):
            soma=soma+a[i,l)
        return(soma)
def scolunas(a):
    soma=0
    for l in range(0,a.shape[1],1):
        for i in range(a.shape[0],1):
            soma=soma+a[i,l]
        return(soma)

