# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Defina a dimensão da matriz:')
x=input('Digite a posição x:')
y=input('Digite a posição y:')

a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Acrescente elementos a lista:')


def somaLinhas(a,x):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[x,j]
        
    return soma
    
def somaColunas(a,y):
    soma=0
    for i in range(0,a.shape[1],1):
        soma=soma+a[i,y]
        
    return soma
    
def peso(a,x,y):
    soma=0
    soma=somaLinhas(a,x)+somaColunas(a,y)-(2*a[x,y])
    return soma
    
    
    
    
    
    
print ('%d' %peso(a,x,y))