# -*- coding: utf-8 -*-
import numpy as np
def somaLinha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return soma
def somaColuna(a,j):
    soma2=0
    for i in range(0,a.shape[0],1):
        soma2=soma2+a[i,j]
    return soma2
def     