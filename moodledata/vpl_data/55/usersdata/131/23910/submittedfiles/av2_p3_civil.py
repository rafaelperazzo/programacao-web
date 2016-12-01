# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np


def smlinha(a,x):
    sm=0
    for j in range(0,a.shape[1],1):
        sm=sm+a[n,j]
    return sm
def smcoluna(a,y):
    sm=0
    for i in range(0,a.shape[0],1):
        sm=sm+a[i,y]
    return sm 
def smtotal(a,x,y):
    sm=0
    sm=smlinha(a,x)+smcoluna(a,y)-(2*a[x,y])
    return sm

n=input('dimensão da matriz:')    
x=input('cordenada das linhas')
y=input('cordenada das colunas')

a=np.zeros ((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input ('digite um numero da matriz :')
        
print('%d' %smtotal(a,x,y))

    