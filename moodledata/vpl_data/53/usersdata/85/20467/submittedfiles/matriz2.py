# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def lista1(a):
    b=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            b.append(a[i,j]
    
    return sum(b)
    
def lista2(a):
    c=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==j:
                c.append(a[i,j])
    return sum(c)
    
def lista3(a):
    d=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if i==(a.shape[1]-j-1):
                d.append(a[i,j]
    return sum(d)

l= input('Digite o número de linhas/colunas: ')
a= np.zeros((l,l))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]= input('Digite o elemento da matriz: ')
        
somal= lista1(a)
somac= lista1(a)
somadp= lista2(a)
somads= lista3(a)

if (somal/l)==(somac/l)==somadp==somads:
    print('S')
else:
    print('N')