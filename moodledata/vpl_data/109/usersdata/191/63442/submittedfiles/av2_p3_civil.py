# -*- coding: utf-8 -*-
import numpy as np
def linhas(c,d):
    soma=0
    for i in range(0,d.shape[1],1):
        soma=soma+d[c,i]
    return(soma)
    
def colunas(c,d):
    soma=0
    for i in range(0,d.shape[0],1):
        soma=soma+d[i,c]
    return soma
    
a=int(input('dimensao da matriz:'))
b=int(input('digite b:'


