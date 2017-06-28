# -*- coding: utf-8 -*-
import numpy as np
def linhas(a,m):
    soma=0
    for i in range(0,m.shape[1],1):
        soma=soma+m[a,i]
    return(soma)
    
def colunas(a,m):
    soma=0
    for i in range(0,shape[0],1):
        soma=soma+m[i,a]
    return(soma)
    
h=int(input('digite a dimensao da matriz:'))
x=int(input('digite x:'))


