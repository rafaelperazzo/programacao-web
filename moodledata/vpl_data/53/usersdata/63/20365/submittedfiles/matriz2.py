# -*- coding: utf-8 -*-
from __future__ import division

def somadiagonal1 (a):
    soma=0
    for i in range (0, a.shape[0], 1):
        soma=soma+a [i,i]
    return soma
    
def somadiagonal2 (a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=i-1
    return soma
