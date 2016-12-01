# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def slinha(a,x):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[x,j]
    return soma

def scoluna(a,y):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
    return soma

def somatorio(a,x,y):
    soma=(slinha(a,x)+scoluna(a,y))-(2*a[x,y])
    return soma
    
n=input('Dê a dimensão da matriz: ')
x=input('Digite a coordenada da linha: ')
y=input('Digite a coordenada da coluna: ')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um elemento da matriz: ')
        
somatotal=somatorio(a,x,y)
print ('%d' %somatotal)




