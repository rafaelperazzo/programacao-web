# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_linha(a,b):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[b,j]
    return soma
    
def soma_coluna(a,d):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,d]
    return soma
    
def soma(a,b,d):
    soma=0
    soma=(soma_linha(a,b)+soma_coluna(a,d))-(2*a[b,d])
    return soma
    
b=input('digite a quantidade de linhas:')
d=input('digite a quantidade de colunas:')
a=np.zeros((b,d)) 

 for i in range (0,a.shape[0],1):
     for j in range(0,shape[1],1):
         a[i,j]= input('digite o elemento:')

st=soma(a,b,d)

print ('%d' %st)