# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def peso(a):
    soma1=0
    soma2=0
    for i in range(0,a.shape[0],1):
        soma1=soma1 + a[i,x]
    for j in range(0, a.shape[1],1):
        soma2=soma2 + a[y,j]
    peso = soma1 + soma2 - 2*a[y,x]
    return peso

n=input('digite o valor da dimensão da matriz:')
y=input('digite a coordenada da coluna da torre:')
x=input('digite a coordenada da linha da torre:')
a=np.zeros[z,z]
for i in range(0,z,1):
    for j in range(0,z,1):
        z[i,j]=input('digite o valor da posição:')

peso1=peso(z,y,x)
print(peso1)
        
