# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a,x,y):
    soma=0
    c=0
    d=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if x==a[i+1,j]
                c=i
            if y==a[j+1]
                d=j
    
    for i in range(c,a.shape[0]+1,1):
        for j in range(d,a.shape[1]+1,1):
            soma=soma+a[i,j]
    return soma-a[c,d]
    
linhas=input('Digite a quantidade de linhas: ')
colunas=input('Digite a quantidade de colunas: ')
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite os elementos da matriz: ')
        
n1=input('Digite o valor da posição x: ')
n2=input('Digite o valor da posição y: ')

matriz=a[i,j]
resultado=peso(a,x,y) 
print matriz
print resultado
        
        






