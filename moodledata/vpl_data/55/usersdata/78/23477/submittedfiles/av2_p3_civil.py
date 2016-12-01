# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

def soamalinhas(a,x):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[x,j]
    return soma
            
def somacolunas(a,y):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
    return soma

def soma(a,x,y):
    soma=somalinhas(a,x)+somacolunas(a,y)-2*(a[x,y])
    return soma

x=input('digite a posição da linha:')
y=input('digite a posição da coluna:')
n=input('digite a dimensão da matriz:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o elemento da matriz:')
    
print('%d'%soma(a,x,y))
