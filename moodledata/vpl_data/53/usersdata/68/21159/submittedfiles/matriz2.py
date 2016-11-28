# -*- coding: utf-8 -*-
from __future__ import division

#DIAGONAL PRINCIPAL
def somaDiagonal1(a):
    soma=0
    for i in range (0, a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
#DIAGONAL SECUNDÁRIA
def somaDiagonal2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma 
    
#SOMA DAS LINHAS (PIOR PARTE)
