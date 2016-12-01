# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#definir somalinha
def somalinha(a,linha):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[linha,j]
    return somalinha
    
#definir somacoluna
def somacoluna(a,coluna):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,coluna]
    return soma
    
# definir peso
def peso(a,linha,coluna):
    peso=somalinha(a,linha)+somacoluna(a,coluna)-(2*a[linha,coluna])
    return peso  


n=input('digite n:')
x=input('digite x:')
y=input('digite y:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
    

print ('%d'%peso(a,x,y))

    
    
